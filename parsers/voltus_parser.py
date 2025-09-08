import re, json, sys
def parse_ir(txt):
  m = re.search(r"IR_drop_pct_max\s*=\s*([0-9\.]+)", txt)
  return {"drop_pct_max": float(m.group(1)) if m else None}
if __name__ == "__main__":
  print(json.dumps(parse_ir(sys.stdin.read()), indent=2))
