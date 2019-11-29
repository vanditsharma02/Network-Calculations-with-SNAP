import snap

Graph = snap.LoadEdgeList(snap.PUNGraph, "p2p-Gnutella04.txt", 0, 1)
x = Graph.GetMxNId()

NIdV = snap.TIntV()
for i in range(0, x):  
	if Graph.IsNode(i):
		NIdV.Add(i)

SubGraph = snap.GetSubGraph(Graph, NIdV)
for EI in SubGraph.Edges():
    print "edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId())

snap.SaveEdgeList(SubGraph, 'p2p-Gnutella04-subgraph.elist')
