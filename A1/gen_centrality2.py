import sys
import snap
import Gnuplot
from numpy import inf
from itertools import product

#Set Seed of SNAP to 42
Rnd = snap.TRnd(42)
Rnd.Randomize()

Graph = snap.LoadEdgeList(snap.PUNGraph, sys.argv[1]+".elist", 0, 1)

nodes = Graph.GetNodes()
edges = Graph.GetEdges()

fil = open(sys.argv[1]+".elist","r")
node_list = set()
line_num = 0
for line in fil:
	if line_num > 2 :	
		a, b = map(int, line.split("	"))  
		node_list.add(a)
		node_list.add(b)
	line_num += 1	
fil.close()

#Degree Centrality

D={}
y = sys.argv[1]+"-degree-centrality.txt"

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

for item in InDegV:
	D[item.GetVal1()] = item.GetVal2()

D = sorted(D.iteritems(), key = lambda x : x[1],reverse=True)

f= open(y,"w+")
f.write("#NId Centrality\r\n")
for NId,value in D: 
    f.write("%d %d\r\n" % (NId,value) )	 
f.close()
#print("Degree Centrality done !")

#Closeness Centrality

D = {}
file_name = sys.argv[1]+"-closeness-centrality.txt"

for i in node_list:	
    count = 0
    for j in node_list:
	if i != j:	
	    count += snap.GetShortPath(Graph, i, j)
    #print i
    D[i] = float(nodes)/float(count)

D = sorted(D.iteritems(), key = lambda x : x[1],reverse=True)

f= open(file_name,"w+")
f.write("#NId Centrality\r\n")
for NId,value in D: 
    f.write("%d %f\r\n" % (NId,value) )	 
f.close()

#print("Closeness Centrality done !")

"""
#Betweenness Centrality

y = sys.argv[1]+"-betweenness-centrality.txt"
f= open(y,"w+")

for k in node_list:	
    for j in node_list:
	for j in node_list:	
	    if i != j:	
	        count += snap.GetShortPath(Graph, i, j)
    print i
    D[i] = float(nodes)/float(count)

D = sorted(D.iteritems(), key = lambda x : x[1],reverse=True)

f= open(file_name,"w+")
f.write("#NId Centrality\r\n")
for NId,value in D: 
    f.write("%d %f\r\n" % (NId,value) )	 
f.close()

print("Closeness Centrality done !")
	
f.close()
"""
