import snap

Graph = snap.LoadEdgeList(snap.PUNGraph, "soc-Epinions1.txt", 0, 1)
x = Graph.GetMxNId()

NIdV = snap.TIntV()
for i in range(0, x):
	if i%2 is 1:    
		if Graph.IsNode(i):
			NIdV.Add(i)

SubGraph = snap.GetSubGraph(Graph, NIdV)
for EI in SubGraph.Edges():
    print "edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId())

snap.SaveEdgeList(SubGraph, 'soc-Epinions1-subgraph.elist')
