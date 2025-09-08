# Floorplanning recipe template for Innovus/ICC2/OpenROAD
# Expect variables: util, macros (name x y orient keepout), ioring_um, channels_um
puts "## Floorplan: util=$util ioring=$ioring_um channels=$channels_um"
foreach m $macros {
lassign $m name x y orient keepout
puts "place_macro $name at ($x,$y) orient=$orient keepout=$keepout"
}
