create_clock -name CLK -period 1.0 [get_ports clk]
set_input_delay 0.2 -clock CLK [get_ports {a[*] b[*]}]
set_output_delay 0.2 -clock CLK [get_ports {y[*]}]
