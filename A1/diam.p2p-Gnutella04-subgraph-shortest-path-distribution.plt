#
# Undirected graph => shortest path. G(10876, 39994). Diam: avg:4.64  eff:5.39  max:10 (Wed Sep  4 19:24:31 2019)
#

set title "Undirected graph => shortest path. G(10876, 39994). Diam: avg:4.64  eff:5.39  max:10"
set key bottom right
set logscale y 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Number of hops"
set ylabel "Number of shortest paths"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'diam.p2p-Gnutella04-subgraph-shortest-path-distribution.png'
plot 	"diam.p2p-Gnutella04-subgraph-shortest-path-distribution.tab" using 1:2 title "" with linespoints pt 6
