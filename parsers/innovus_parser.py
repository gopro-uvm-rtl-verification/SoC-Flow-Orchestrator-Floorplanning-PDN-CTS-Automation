import re, json, sys
def parse_congestion(txt):
  m = re.search(r"GRC_overflow_pct\s*=\s*([0-9\.]+)", txt)
  return {"grc_overflow_pct": float(m.group(1)) if m else None}
if __name__ == "__main__":
  print(json.dumps(parse_congestion(sys.stdin.read()), indent=2))
