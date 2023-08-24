import DisjointSet as dst
class Graph:
    def __init__(self,vertices):
        self.V=vertices
        self.graph=[]
        self.nodes=[]
        self.MST=[]

    def addEdge(self,s,d,w):
        self.graph.append([s,d,w])

    def addNode(self,value):
        self.nodes.append(value)

    def printSolution(self,s,d,w):
        for s,d,w in self.MST:
            print("%s - -%s: %s"%(s,d,w))

    def kruskalAlgo(self):
        i,e=0,0
        ds=dst.DisjointSet(self.nodes)
        self.graph=sorted(self.graph,key=lambda item:item[2])
        while e<self.V-1:
            s,d,w=self.graph[i]
            i+=1
            x=ds.find(s)
            y=ds.find(d)
            if x!=y:
                e+=1
                self.MST.append([s,d,w])
                ds.union(x,y)
        self.printSolution(s,d,w)