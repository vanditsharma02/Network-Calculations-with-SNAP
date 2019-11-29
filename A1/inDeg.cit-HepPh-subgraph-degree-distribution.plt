#
# Undirected graph => in-degree Distribution. G(16608, 103954). 5471 (0.3294) nodes with in-deg > avg deg (12.5), 1849 (0.1113) with >2*avg.deg (Wed Sep  4 19:20:18 2019)
#

set title "Undirected graph => in-degree Distribution. G(16608, 103954). 5471 (0.3294) nodes with in-deg > avg deg (12.5), 1849 (0.1113) with >2*avg.deg"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "In-degree"
set ylabel "Count"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'inDeg.cit-HepPh-subgraph-degree-distribution.png'
plot 	"inDeg.cit-HepPh-subgraph-degree-distribution.tab" using 1:2 title "" with linespoints pt 6
