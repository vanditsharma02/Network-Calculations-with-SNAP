import snap

Graph = snap.LoadEdgeList(snap.PUNGraph, "email-Enron.txt", 0, 1)
x = Graph.GetMxNId()


NIdV = snap.TIntV()
for i in range(0, x):
	if i%3 is 0:    
		if Graph.IsNode(i):
			NIdV.Add(i)

SubGraph = snap.GetSubGraph(Graph, NIdV)
for EI in SubGraph.Edges():
    print "edge (%d %d)" % (EI.GetSrcNId(), EI.GetDstNId())

snap.SaveEdgeList(SubGraph, 'email-Enron-subgraph.elist')
