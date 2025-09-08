import re, json, sys
def parse_drc(txt):
  m = re.search(r"DRC_count\s*=\s*([0-9]+)", txt)
  return {"count": int(m.group(1)) if m else None}


def parse_lvs(txt):
  m = re.search(r"LVS\s*=\s*(\w+)", txt)
  return {"status": m.group(1).lower() if m else "dirty"}


if __name__ == "__main__":
  data = sys.stdin.read()
  print(json.dumps({"drc": parse_drc(data), "lvs": parse_lvs(data)}, indent=2))
