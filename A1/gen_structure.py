import sys
import snap
import Gnuplot
import numpy

#Set Seed of SNAP to 42
Rnd = snap.TRnd(42)
Rnd.Randomize()

Graph = snap.LoadEdgeList(snap.PUNGraph, sys.argv[1]+".elist", 0, 1)

nodes = Graph.GetNodes()
edges = Graph.GetEdges()

print "Number of nodes in",sys.argv[1], ":",nodes
print "Number of edges in",sys.argv[1], ":",edges

InDegV = snap.TIntPrV()
snap.GetNodeInDegV(Graph, InDegV)

#No. of nodes with Degree = 7 
count = 0
maxdegree = 0

for item in InDegV:
	if item.GetVal2() is 7:
		count=count+1
	
print "Number of nodes with degree=7 in",sys.argv[1], ":",count

#Node id(s) for the node with the highest degree
for item in InDegV:
	if item.GetVal2() > maxdegree:
		maxdegree = item.GetVal2()

x = "Node id(s) with highest degree in "+sys.argv[1]+" : "
for item in InDegV:
	if item.GetVal2() == maxdegree:
		x = x+str(item.GetVal1())+", "

x = x[:-2]
print x

#Plot of Degree Distribution
y = sys.argv[1]+"-degree-distribution"
snap.PlotInDegDistr(Graph, y, "Undirected graph => in-degree Distribution")
print "Degree distribution of",sys.argv[1],"is in:",y+".png"

#Approximate full diameter

array = []

diameter1 = snap.GetBfsFullDiam(Graph, 10, False)
array.append(diameter1)
diameter2 = snap.GetBfsFullDiam(Graph, 100, False)
array.append(diameter2)
diameter3 = snap.GetBfsFullDiam(Graph, 1000, False)
array.append(diameter3)

mean = numpy.mean(array)
variance = (numpy.std(array))**2

print "Approximate full diameter in",sys.argv[1],"with sampling 10 nodes:",diameter1
print "Approximate full diameter in",sys.argv[1],"with sampling 100 nodes:",diameter2
print "Approximate full diameter in",sys.argv[1],"with sampling 1000 nodes:",diameter3
print "Approximate full diameter in",sys.argv[1],"with sampling nodes (mean and variance):",mean,",",variance

#Approximate effective diameter

array = []

diameter1 = snap.GetBfsEffDiam(Graph, 10, False)
array.append(diameter1)
diameter2 = snap.GetBfsEffDiam(Graph, 100, False)
array.append(diameter2)
diameter3 = snap.GetBfsEffDiam(Graph, 1000, False)
array.append(diameter3)

mean = numpy.mean(array)
variance = (numpy.std(array))**2

print "Approximate effective diameter in",sys.argv[1],"with sampling 10 nodes:",diameter1
print "Approximate effective diameter in",sys.argv[1],"with sampling 100 nodes:",diameter2
print "Approximate effective diameter in",sys.argv[1],"with sampling 1000 nodes:",diameter3
print "Approximate effective diameter in",sys.argv[1],"with sampling nodes (mean and variance):",mean,",",variance

#Plot of distribution of shortest path lengths in network
y = sys.argv[1]+"-shortest-path-distribution"
snap.PlotShortPathDistr(Graph, y, "Undirected graph => shortest path")
print "Shortest path distribution of",sys.argv[1],"is in:",y+".png"

#Fraction of nodes in the largest connected component

print "Fraction of nodes in largest connected component in",sys.argv[1],":", snap.GetMxSccSz(Graph)

#Number of edge bridges

EdgeV = snap.TIntPrV()
snap.GetEdgeBridges(Graph, EdgeV)
count = 0
for edge in EdgeV:
    count = count + 1

print "Number of edge bridges in",sys.argv[1],":",count

#Number of articulation points

ArtNIdV = snap.TIntV()
snap.GetArtPoints(Graph, ArtNIdV)
count = 0
for NI in ArtNIdV:
    count = count + 1

print "Number of articulation points in",sys.argv[1],":",count

#Plot of the distribution of size of connected components
y = sys.argv[1]+"-scc-size-distribution"
snap.PlotSccDistr(Graph, y, "Undirected graph => scc distribution")
print "Component size distribution of",sys.argv[1],"is in:",y+".png"

#Average clustering coefficient of the network

acc = snap.GetClustCf (Graph, -1)
print "Average clustering coefficient in",sys.argv[1],":",round(acc,4)  

#Number of triads

triads = snap.GetTriads(Graph)
print "Number of triads in",":",triads

#Clustering coefficient of a randomly selected node

nodeid= Graph.GetRndNId()
cc = snap.GetNodeClustCf(Graph, nodeid)
print "Clustering coefficient of random node",nodeid,"in",sys.argv[1],":",cc

#Number of triads a randomly selected node participates in

nodeid= Graph.GetRndNId()
nodetriads = snap.GetNodeTriads(Graph,nodeid)
print "Number of triads random node",nodeid,"participates in",sys.argv[1],":",nodetriads

#Number of edges that participate in at least one triad

NumTriadEdges = snap.GetTriadEdges(Graph)
print "Number of edges that participate in at least one triad in",sys.argv[1],":",NumTriadEdges

#Plot of the distribution of clustering coefficient

y = sys.argv[1]+"-clustering-coefficient-distribution"
snap.PlotClustCf(Graph, y, "Undirected graph => clustering coefficient")
print "Clustering coefficient distribution of",sys.argv[1],"is in:",y+".png"
















