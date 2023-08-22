from collections import defaultdict

class Graph:
    def __init__(self,numberOfVertices):
        self.graph=defaultdict(list)
        self.numberOfVertices=numberOfVertices

    def addEdge(self,vertex,edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)
        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v)

    def topologicalSort(self):
        visited=[]
        stack={}
        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)

        print(stack)
