#
# Undirected graph => shortest path. G(27407, 102004). Diam: avg:4.29  eff:5.02  max:13 (Wed Sep  4 19:19:41 2019)
#

set title "Undirected graph => shortest path. G(27407, 102004). Diam: avg:4.29  eff:5.02  max:13"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.soc-Epinions1-subgraph-shortest-path-distribution.png'
plot 	"diam.soc-Epinions1-subgraph-shortest-path-distribution.tab" using 1:2 title "" with linespoints pt 6
