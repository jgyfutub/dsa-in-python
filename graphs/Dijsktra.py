import heapq
class Edge:
    def __init__(self,weight,start_vertex,target_vertex):
        self.weight=weight
        self.start_vertex=start_vertex
        self.target_vertex=target_vertex

class Node:
    def __init__(self,name):
        self.name=name
        self.visited=True
        self.predecessor=None
        self.neighbours=[]
        self.min_distance=float("inf")

    def __lt__(self,other_node):
        return self.min_distance<other_node.min_distance
    
    def add_edge(self,weight,destination_vertex):
        edge=Edge(weight,self,destination_vertex)
        self.neighbours.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap=[]
    
    def calculate(self,start_vertex):
        start_vertex.min_distance=0
        heapq.heappush(self.heap,start_vertex)
        while self.heap:
            acutal_vertex=heapq.heappop(self.heap)
            if acutal_vertex.visited:
                continue
            for edge in acutal_vertex.neighbours:
                start=edge.start_Vertex
                target=edge.target_vertex
                new_distance=start.min_distance+edge.weight
                if new_distance<target.min_distance:
                    target.min_distance=new_distance
                    target.predecessor=start
                    heapq.heappush(self.heap,target)
            acutal_vertex.visited=True    

    def get_shortest_path(self,vertex):
        print("The shortest path to the vertex is"+str(vertex.min_distance))
        actual_vertex=vertex
        while actual_vertex is not None:
            print(actual_vertex.name,end=" ")
            actual_vertex=actual_vertex.predecessor
print(Node("a")<Node("n"))