#
# Undirected graph => scc distribution. G(16608, 103954). Largest component has 0.988500 nodes (Wed Sep  4 19:22:12 2019)
#

set title "Undirected graph => scc distribution. G(16608, 103954). Largest component has 0.988500 nodes"
set key bottom right
set logscale xy 10
set format x "10^{%L}"
set mxtics 10
set format y "10^{%L}"
set mytics 10
set grid
set xlabel "Size of strongly connected component"
set ylabel "Number of components"
set tics scale 2
set terminal png font arial 10 size 1000,800
set output 'scc.cit-HepPh-subgraph-scc-size-distribution.png'
plot 	"scc.cit-HepPh-subgraph-scc-size-distribution.tab" using 1:2 title "" with linespoints pt 6
