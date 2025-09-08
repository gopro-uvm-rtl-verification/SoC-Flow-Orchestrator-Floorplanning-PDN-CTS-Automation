
# SoC Flow Orchestrator — Floorplanning/PDN/CTS Automation (Tcl/Python)

This is a **complete, educational example** of the project on your résumé.
It demonstrates a **node-agnostic flow driver** with **report adapters**, **quality gates**, and **baseline diffs**.

Two modes:
- **mock**: runnable without EDA tools (default).
- **real**: use your tools + runsets (requires licenses).

## Quickstart (mock)

```
python3 flow.py --cfg configs/socA_5nm.yml --mode mock
.
├── README.md
├── LICENSE
├── flow.py
├── gates.py
├── baseline.py
├── configs/
│ └── socA_5nm.yml
├── scripts/
│ ├── floorplan.tcl
│ ├── pdn.tcl
│ ├── place.tcl
│ ├── cts.tcl
│ ├── route.tcl
│ ├── sta.tcl
│ ├── ir_em.tcl
│ └── drc_lvs.tcl
├── adapters/
│ ├── innovus.py
│ ├── primetime.py
│ ├── tempus.py
│ ├── voltus.py
│ ├── calibre.py
│ ├── openroad.py
│ └── pdnsim.py
├── parsers/
│ ├── pt_parser.py
│ ├── innovus_parser.py
│ ├── voltus_parser.py
│ ├── calibre_parser.py
│ └── pdnsim_parser.py
├── schemas/
│ └── summary.schema.json
├── sample_inputs/
│ ├── netlist.v
│ └── base.sdc
├── out/ # (generated)
├── reports/ # (generated)
└── baseline/ # (generated)
```

Artifacts:
- `out/*`  — stage artifacts
- `reports/*` — raw reports
- `reports/summary.json|csv` — normalized result
- `reports/gates.txt` — PASS/FAIL
- `baseline/` — baseline for delta


