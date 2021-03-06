#
# Undirected graph => clustering coefficient. G(7275, 18453). Average clustering: 0.2884  OpenTriads: 713482 (0.9685)  ClosedTriads: 23202 (0.0315) (Wed Sep  4 19:23:18 2019)
#

set title "Undirected graph => clustering coefficient. G(7275, 18453). Average clustering: 0.2884  OpenTriads: 713482 (0.9685)  ClosedTriads: 23202 (0.0315)"
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
set output 'ccf.email-Enron-subgraph-clustering-coefficient-distribution.png'
plot 	"ccf.email-Enron-subgraph-clustering-coefficient-distribution.tab" using 1:2 title "" with linespoints pt 6
