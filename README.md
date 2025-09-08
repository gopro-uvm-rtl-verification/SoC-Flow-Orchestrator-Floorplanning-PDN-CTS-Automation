
# SoC Flow Orchestrator — Floorplanning/PDN/CTS Automation (Tcl/Python)

This is a **complete, educational example** of the project on your résumé.
It demonstrates a **node-agnostic flow driver** with **report adapters**, **quality gates**, and **baseline diffs**.

Two modes:
- **mock**: runnable without EDA tools (default).
- **real**: use your tools + runsets (requires licenses).

## Quickstart (mock)

```
python3 flow.py --cfg configs/socA_5nm.yml --mode mock
```

Artifacts:
- `out/*`  — stage artifacts
- `reports/*` — raw reports
- `reports/summary.json|csv` — normalized result
- `reports/gates.txt` — PASS/FAIL
- `baseline/` — baseline for delta
