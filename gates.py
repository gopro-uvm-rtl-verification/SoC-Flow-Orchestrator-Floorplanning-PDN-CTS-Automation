
def check_gates(cfg, summary):
    g = cfg["gates"]; msgs = []; ok = True
    def req(cond, msg):
        nonlocal ok; msgs.append(("OK: " if cond else "FAIL: ") + msg)
        if not cond: ok = False
    t, ir, drc, lvs, cong, pwr = summary["timing"], summary["ir"], summary["drc"], summary["lvs"], summary["congestion"], summary["power"]
    req(t["WNS_ps"] >= g["wns_ps_min"], f"WNS_ps >= {g['wns_ps_min']} (got {t['WNS_ps']})")
    req(t["TNS_ns"] <= g["tns_ns_max"], f"TNS_ns <= {g['tns_ns_max']} (got {t['TNS_ns']})")
    req(ir["drop_pct_max"] <= g["ir_drop_pct_max"], f"IR_drop_pct_max <= {g['ir_drop_pct_max']} (got {ir['drop_pct_max']})")
    req(drc["count"] <= g["drc_max"], f"DRC_count <= {g['drc_max']} (got {drc['count']})")
    req(lvs["status"].lower() == g["lvs_must_be"], f"LVS == {g['lvs_must_be']} (got {lvs['status']})")
    req(cong["grc_overflow_pct"] <= g["grc_overflow_pct_max"], f"GRC_overflow_pct <= {g['grc_overflow_pct_max']} (got {cong['grc_overflow_pct']})")
    req(pwr["clock_mw"] <= g["clock_power_mw_max"], f"clock_power_mw <= {g['clock_power_mw_max']} (got {pwr['clock_mw']})")
    return ok, msgs
