# 这个功能是输出CTS报告，具体是什么样的buffers、skew、insertion和useful_skew
puts "## CTS: buffers=$buffers skew=$skew_ps insertion=$insertion_ps useful_skew=$useful_skew"  
# build clock tree; check clock gating; report skew/insertion/power -> reports/clock.rpt

#这个功能是输出DRC和LVS报告，具体是什么样的DRC/LVS规则
puts "## DRC/LVS -> reports/calibre_drc.rpt & reports/calibre_lvs.rpt"  

# 这个功能是输出Floorplan报告，具体是什么样的utilization、IR ring和channels
puts "## Floorplan: util=$util ioring=$ioring_um channels=$channels_um"
foreach m $macros {
lassign $m name x y orient keepout
puts "place_macro $name at ($x,$y) orient=$orient keepout=$keepout"
}

# 这个功能是输出IR/EM报告，具体是什么样的电源网络拓扑结构
puts "## IR/EM signoff -> reports/ir_em.rpt"

# 这个功能是输出PDN报告，具体是什么样的风格、via堆栈和decap比例
puts "## PDN: style=$style via_stack=$via_stack decap_ratio=$decap_ratio" 
# foreach strap: layer/pitch/width
# generate rings/mesh; add vias; place decaps; export reports/ir_em.rpt

#这个功能是输出Placement报告，具体是什么样的utilization和density
puts "## Placement: max_util=$max_util" 
# place_opt -congestion_driven true
# trial_route -> reports/congestion.rpt

# 这个功能是输出Power报告，具体是什么样的rail和via
puts "## Route: prefer_layers=$prefer_layers shield_critical=$shield_critical"
# global_route; detail_route; fix_drc -> reports/route.drc

# 这个功能是输出STA报告，具体是什么样的sweep和timing
puts "## STA: MMMC sweep and report -> reports/pt_timing.rpt"
