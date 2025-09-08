import re, json, sys
def parse_pt(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"\s*WNS_ps\s*=\s*([-0-9\.]+)", line)
        if m: out["WNS_ps"] = float(m.group(1))
        m = re.match(r"\s*TNS_ns\s*=\s*([-0-9\.]+)", line)
        if m: out["TNS_ns"] = float(m.group(1))
        m = re.match(r"\s*viol_paths\s*=\s*([0-9]+)", line)
        if m: out["viol_paths"] = int(m.group(1))
    return out
if __name__ == "__main__":
    print(json.dumps(parse_pt(sys.stdin.read()), indent=2))
