import sys
import snap
import Gnuplot

#Set Seed of SNAP to 42
Rnd = snap.TRnd(42)
Rnd.Randomize()

Graph = snap.LoadEdgeList(snap.PUNGraph, sys.argv[1]+".elist", 0, 1)

#Closeness Centrality

D = {}
for NI in Graph.Nodes():
    D[NI.GetId()] = snap.GetClosenessCentr(Graph, NI.GetId())

D = sorted(D.iteritems(), key = lambda x : x[1],reverse=True)

node_list_cc = set()
count = 0
for NId,value in D:
    node_list_cc.add(NId)
    #print "node: %d centrality: %f" % (NId, value)
    count += 1
    if count is 10:
	break	

#print("Closeness Centrality done !")
#print(node_list_cc)

#Betweenness Centrality

Nodes = snap.TIntFltH()
Edges = snap.TIntPrFltH()
snap.GetBetweennessCentr(Graph, Nodes, Edges, 0.8)

D={}
for node in Nodes:
	D[node] = Nodes[node]

D = sorted(D.iteritems(), key = lambda x : x[1],reverse=True)

node_list_bc = set()
count = 0
for NId,value in D:
    node_list_bc.add(NId)
    #print "node: %d centrality: %f" % (NId, value)
    count += 1
    if count is 10:
	break	

#print(node_list_bc)

#Number of overlaps


fil = open(sys.argv[1]+"-closeness-centrality.txt","r")
node_list_cc_calculated = set()
line_num = 0

for line in fil:
	if line_num > 0 :	
		a, b = line.split(" ") 
                a = int(a,10)  
		node_list_cc_calculated.add(a)
	line_num += 1	
	if line_num is 11:
		break
fil.close()

value = len(node_list_cc.intersection(node_list_cc_calculated))
print "Number of overlaps for Closeness Centrality:",value

fil = open(sys.argv[1]+"-betweenness-centrality.txt","r")
node_list_bc_calculated = set()
line_num = 0

for line in fil:
	if line_num > 0 :	
		a, b = line.split(" ") 
                a = int(a,10)  
		node_list_bc_calculated.add(a)
	line_num += 1	
	if line_num is 11:
		break
fil.close()

value = len(node_list_bc.intersection(node_list_bc_calculated))
print "Number of overlaps for Betweenness Centrality:",value
