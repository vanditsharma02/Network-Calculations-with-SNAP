#
# Undirected graph => shortest path. G(16608, 103954). Diam: avg:4.86  eff:5.89  max:16 (Wed Sep  4 19:22:11 2019)
#

set title "Undirected graph => shortest path. G(16608, 103954). Diam: avg:4.86  eff:5.89  max:16"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.cit-HepPh-subgraph-shortest-path-distribution.png'
plot 	"diam.cit-HepPh-subgraph-shortest-path-distribution.tab" using 1:2 title "" with linespoints pt 6
