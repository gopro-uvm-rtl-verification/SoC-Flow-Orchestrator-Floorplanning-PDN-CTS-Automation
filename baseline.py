
def diff_summaries(before, after): #比较前后summary，计算关键指标的变化，返回变化字典
    def gv(d, path, default=None): #根据路径获取嵌套字典的值
        for k in path.split("."):
            d = d.get(k, {})
        return d if d != {} else default
    keys = [
        "timing.WNS_ps","timing.TNS_ns",
        "ir.drop_pct_max","drc.count","lvs.status",
        "power.clock_mw","congestion.grc_overflow_pct"
    ]
    out = {"deltas": {}}
    for k in keys:
        b = gv(before, k); a = gv(after, k)
        if isinstance(b,(int,float)) and isinstance(a,(int,float)):
            out["deltas"][k] = a - b
        else:
            out["deltas"][k] = f"{b} -> {a}"
    return out
