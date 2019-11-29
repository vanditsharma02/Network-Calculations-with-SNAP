#
# Undirected graph => clustering coefficient. G(16608, 103954). Average clustering: 0.2616  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510) (Wed Sep  4 19:22:12 2019)
#

set title "Undirected graph => clustering coefficient. G(16608, 103954). Average clustering: 0.2616  OpenTriads: 2806109 (0.9490)  ClosedTriads: 150897 (0.0510)"
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
set output 'ccf.cit-HepPh-subgraph-clustering-coefficient-distribution.png'
plot 	"ccf.cit-HepPh-subgraph-clustering-coefficient-distribution.tab" using 1:2 title "" with linespoints pt 6
