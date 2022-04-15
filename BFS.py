from collections import deque
class Vertex:
    def __init__(self, name):
        self.name = name
        self.discovered = False
        self.neighbors = list()
        
    def add_neighbor(self, v):
        nset = set(self.neighbors)
        if v not in nset:
            self.neighbors.append(v)
            self.neighbors.sort()
            
class Graph:
    def __init__(self, edges, vertices, N):
        self.adjList = [[] for _ in range(N)]
        self.vertices = vertices
        
        for (src, dest) in edges:
            self.adjList[src].append(dest)
           
            self.vertices.append(src)
            self.vertices.append(dest)
        self.vertices = set(self.vertices)
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neigbour(v)
                if key == v:
                    value.add_neigbour(u) 
    def print_graph(self, adj):
        for (src, dest)in sorted(list(self.adj)):
            print(src + " -> "+str(dest))
    

    
    def dfs(self):
        self.visited = len(self.vertices) * [False]
        self.res = list()
        for i in range(len(self.vertices)):
            if self.visited[i]==False:
                self._dfs(i, self.vertices, self.adjList, self.visited, self.res)
     
    def _dfs(self, i, vertices, adj, visited, res):
        if self.visited[i]: return
        self.visited[i] = True
        self.res.append(i)
        print(str(i)+" -> ")
        for j in range(0, len(adj[i])):
            if self.visited[adj[i][j]] == False:
                _dfs(adj[i][j], self.vertices, self.adjList, self.visited, self.res)
                
    
            
            
def recursiveBFS(graph, q, discovered):
    if not q:
        return
    
    v = q.popleft()
    print(v, end=' ')
    
    for u in graph.adjList[v]:
        if not discovered[u]:
            discovered[u] = True
            q.append(u)
            
    recursiveBFS(graph, q, discovered)
    
    
if __name__ == "__main__":
    edges = [
         (1,2), (1,3), (1,4), (2,5), (2,6), (5,9),
        (5,10), (4,7), (4,8), (7,11), (7,12),
     ]
    N = 15 
    vertices = list()
    graph = Graph(edges, vertices, N)
    print(graph.adjList)
    graph.dfs()
    """
     for i in range(ord('A'), ord('K'), 2):
         u = Vertex(chr(i))
         v = Vertex(chr(i+1))
         graph.add_vertex(u)
         graph.add_vertex(v)
         graph.add_edge(u, v)
     graph.print_graph()
    
    discovered = [False] * N
    q = deque()
    
    for i in range(N):
        if not discovered[i]:
              discovered[i]=True
              q.append(i)
              recursiveBFS(graph, q, discovered)
              """
   
 

