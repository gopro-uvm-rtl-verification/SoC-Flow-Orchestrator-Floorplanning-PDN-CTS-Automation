# 定义主时钟 —— 决定频率（这里 1.00ns = 1GHz）
create_clock -name core_clk -period 1.00 [get_ports clk]

# 时钟不确定度 —— 安全垫（越大越难过时序，常见 0.04~0.08ns）
# 先给 0.06ns 试跑；如果你现在是 0.12ns，建议先收紧
set_clock_uncertainty 0.06 [get_clocks core_clk]

# 输入/输出时序 —— 防止“假绿”（板级对接的真实时间要求）
set_input_delay  0.20 -clock core_clk [get_ports din*]    ;# 输入延迟示例
set_output_delay 0.25 -clock core_clk [get_ports dout*]   ;# 输出延迟示例

# 输出负载 —— 外部负载（没写会过于乐观）
set_load 0.004 [get_ports dout*]                          ;# 约 4pF 等效
