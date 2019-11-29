#
# Directed graph => in-degree Distribution. G(27407, 128201). 2307 (0.0842) nodes with in-deg > avg deg (9.4), 1337 (0.0488) with >2*avg.deg (Fri Aug 23 17:04:30 2019)
#

set title "Directed graph => in-degree Distribution. G(27407, 128201). 2307 (0.0842) nodes with in-deg > avg deg (9.4), 1337 (0.0488) with >2*avg.deg"
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
set output 'inDeg.soc-Epinions1-subgraph-degree-distribution.png'
plot 	"inDeg.soc-Epinions1-subgraph-degree-distribution.tab" using 1:2 title "" with linespoints pt 6
