module top(input clk, input rstn, input [7:0] a, b, output [7:0] y);
  reg [7:0] r;
  always @(posedge clk or negedge rstn) begin
    if(!rstn) r <= 0; else r <= a + b;
  end
  assign y = r;
endmodule
