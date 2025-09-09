
def check_gates(cfg, summary): #检查门限条件，返回是否通过和消息列表
    g = cfg["gates"]; msgs = []; ok = True
    def req(cond, msg): #检查单个条件
        nonlocal ok; msgs.append(("OK: " if cond else "FAIL: ") + msg) #添加消息
        if not cond: ok = False #如果条件不满足，设置ok为False
    t, ir, drc, lvs, cong, pwr = summary["timing"], summary["ir"], summary["drc"], summary["lvs"], summary["congestion"], summary["power"] #提取各个部分的结果
    req(t["WNS_ps"] >= g["wns_ps_min"], f"WNS_ps >= {g['wns_ps_min']} (got {t['WNS_ps']})") #检查时序门限, WNS_ps >= wns_ps_min
    req(t["TNS_ns"] <= g["tns_ns_max"], f"TNS_ns <= {g['tns_ns_max']} (got {t['TNS_ns']})") #检查时序门限, TNS_ns <= tns_ns_max
    req(ir["drop_pct_max"] <= g["ir_drop_pct_max"], f"IR_drop_pct_max <= {g['ir_drop_pct_max']} (got {ir['drop_pct_max']})") #检查IR门限
    req(drc["count"] <= g["drc_max"], f"DRC_count <= {g['drc_max']} (got {drc['count']})") #检查DRC门限
    req(lvs["status"].lower() == g["lvs_must_be"], f"LVS == {g['lvs_must_be']} (got {lvs['status']})") #检查LVS门限
    req(cong["grc_overflow_pct"] <= g["grc_overflow_pct_max"], f"GRC_overflow_pct <= {g['grc_overflow_pct_max']} (got {cong['grc_overflow_pct']})") #检查拥塞门限
    req(pwr["clock_mw"] <= g["clock_power_mw_max"], f"clock_power_mw <= {g['clock_power_mw_max']} (got {pwr['clock_mw']})") #检查功耗门限
    return ok, msgs
