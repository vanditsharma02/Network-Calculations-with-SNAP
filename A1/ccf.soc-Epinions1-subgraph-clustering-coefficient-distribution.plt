#
# Undirected graph => clustering coefficient. G(27407, 102004). Average clustering: 0.1063  OpenTriads: 8596609 (0.9748)  ClosedTriads: 221969 (0.0252) (Wed Sep  4 19:19:42 2019)
#

set title "Undirected graph => clustering coefficient. G(27407, 102004). Average clustering: 0.1063  OpenTriads: 8596609 (0.9748)  ClosedTriads: 221969 (0.0252)"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Node degree"
set ylabel "Average clustering coefficient"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'ccf.soc-Epinions1-subgraph-clustering-coefficient-distribution.png'
plot 	"ccf.soc-Epinions1-subgraph-clustering-coefficient-distribution.tab" using 1:2 title "" with linespoints pt 6
