
import argparse, json, os, csv #这个地方是import，功能是导入所需的模块
from pathlib import Path
import yaml
from baseline import diff_summaries
from gates import check_gates

def load_cfg(p):#加载配置文件，返回配置字典，使用yaml.safe_load
    with open(p, "r") as f:
        return yaml.safe_load(f)

def ensure_dirs(cfg):#确保工作目录和报告目录存在
    Path(cfg["paths"]["workdir"]).mkdir(parents=True, exist_ok=True)
    Path(cfg["paths"]["reportdir"]).mkdir(parents=True, exist_ok=True)

def write_file(p, text):#·写文件，确保目录存在
    Path(p).parent.mkdir(parents=True, exist_ok=True)
    with open(p, "w") as f:
        f.write(text)

def mock_stage(name, cfg):#模拟各个设计阶段，生成假文件和报告
    out = Path(cfg["paths"]["workdir"])
    rep = Path(cfg["paths"]["reportdir"])
    if name == "floorplan":
        write_file(out / "floorplan.def", "# mock DEF floorplan\n")
        write_file(rep / "congestion.rpt", "GRC_overflow_pct = 0.8\n")
    elif name == "pdn":
        write_file(out / "pdn.def", "# mock PDN DEF\n")
        write_file(rep / "ir_em.rpt", "IR_drop_pct_max = 3.7\nEM_status = pass\n")
    elif name == "place":
        write_file(out / "placed.def", "# mock placed DEF\n")
    elif name == "cts":
        write_file(out / "cts.def", "# mock CTS DEF\n")
        write_file(rep / "clock.rpt", "skew_ps = 38\ninsertion_ps = 820\nclock_power_mw = 96.2\n")
    elif name == "route":
        write_file(out / "routed.def", "# mock routed DEF\n")
        write_file(rep / "route.drc", "DRC_count = 0\n")
    elif name == "signoff":
        write_file(rep / "pt_timing.rpt", "WNS_ps = 12.3\nTNS_ns = 0.0\nviol_paths = 0\n")
        write_file(rep / "calibre_drc.rpt", "DRC_count = 0\n")
        write_file(rep / "calibre_lvs.rpt", "LVS = clean\n")

def parse_and_summarize(cfg):#解析各个报告文件，汇总结果，生成summary.json和summary.csv
    rep = Path(cfg["paths"]["reportdir"])

    def read_kv(p):
        d = {}
        if not p.exists(): return d
        for line in open(p):
            if "=" in line:
                k,v = line.strip().split("=")
                d[k.strip()] = v.strip()
        return d

    t = read_kv(rep / "pt_timing.rpt")
    ir = read_kv(rep / "ir_em.rpt")
    clk = read_kv(rep / "clock.rpt")
    drc = read_kv(rep / "calibre_drc.rpt")
    lvs = read_kv(rep / "calibre_lvs.rpt")
    cong = read_kv(rep / "congestion.rpt")

    summary = {
        "timing": {
            "WNS_ps": float(t.get("WNS_ps", "-1")),
            "TNS_ns": float(t.get("TNS_ns", "0")),
            "viol_paths": int(t.get("viol_paths", "0")),
        },
        "power": {
            "clock_mw": float(clk.get("clock_power_mw", "0")),
            "total_mw": float(clk.get("clock_power_mw", "0")) + 317.3
        },
        "ir": {"drop_pct_max": float(ir.get("IR_drop_pct_max", "9.9"))},
        "drc": {"count": int(drc.get("DRC_count", "999"))},
        "lvs": {"status": lvs.get("LVS", "dirty")},
        "congestion": {"grc_overflow_pct": float(cong.get("GRC_overflow_pct", "5.0"))}
    }

    (rep / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    with open(rep / "summary.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["metric","value"])
        for k,v in [
            ("WNS_ps", summary["timing"]["WNS_ps"]),
            ("TNS_ns", summary["timing"]["TNS_ns"]),
            ("viol_paths", summary["timing"]["viol_paths"]),
            ("clock_power_mw", summary["power"]["clock_mw"]),
            ("power_total_mw", summary["power"]["total_mw"]),
            ("IR_drop_pct_max", summary["ir"]["drop_pct_max"]),
            ("DRC_count", summary["drc"]["count"]),
            ("LVS", summary["lvs"]["status"]),
            ("GRC_overflow_pct", summary["congestion"]["grc_overflow_pct"]),
        ]: w.writerow([k,v])
    return summary

def main():#主函数，解析命令行参数，执行各个设计阶段，汇总结果，检查门限，生成报告，处理基线，退出
    ap = argparse.ArgumentParser()
    ap.add_argument("--cfg", required=True)
    ap.add_argument("--mode", choices=["mock","real"], default="mock")
    args = ap.parse_args()

    cfg = load_cfg(args.cfg)
    ensure_dirs(cfg)

    stages = ["floorplan","pdn","place","cts","route","signoff"]
    for s in stages:
        print(f"[flow] Stage: {s}")
        mock_stage(s, cfg) if args.mode == "mock" else mock_stage(s, cfg)  # replace with adapters for real

    print("[flow] Summarizing...")
    summary = parse_and_summarize(cfg)

    print("[flow] Checking gates...")
    passed, messages = check_gates(cfg, summary)
    Path(cfg["paths"]["reportdir"], "gates.txt").write_text(
        "\n".join([("PASS" if passed else "FAIL")] + messages),
        encoding="utf-8"
    )
    for m in messages: print(" -", m)
    print("[flow]", "PASS" if passed else "FAIL")

    # Baseline
    bdir = Path("baseline"); bdir.mkdir(exist_ok=True)
    bsum = bdir / "summary.json"
    if not bsum.exists():
        bsum.write_text(json.dumps(summary, indent=2), encoding="utf-8")
        print("[baseline] Created new baseline.")
    else:
        before = json.loads(bsum.read_text(encoding="utf-8"))
        from baseline import diff_summaries
        delta = diff_summaries(before, summary)
        Path(cfg["paths"]["reportdir"], "delta_vs_baseline.json").write_text(
            json.dumps(delta, indent=2), encoding="utf-8"
        )
        print("[baseline] Wrote delta_vs_baseline.json")

if __name__ == "__main__":
    main()
