import graph
sep = '-'

def IDDFS(graph, vertex, target, max_search_depth=20):
    for search_depth in range(max_search_depth+1):
        print(f'Iteration started, search depth: {search_depth}')
        result, remaining = DFS(graph, vertex, target, search_depth)
    print(f'Iteration ended.')
    print(2*'\n')
    if result is not None:
        return result
    elif not remaining:
        return None

def DFS(graph, vertex, search_depth, target=None, drawing_path=1):
    print(sep*drawing_depth +f'Exploring vertex: {vertex}')
    result = None
    path.append(vertex.entity())
    if search_depth == 0:
        if target is None:
            print(f'Target vertex {target} does not exist')
            return None, False
        elif vertex == target:
            result = vertex
            return result, True
        else:
            path.pop()
            return None, True
    elif search_depth > 0:
        any_remaining = False
        for edge in g.adjacent_edges(vertex):
            v2nd_endpoint = edge.opposite(vertex)
            if v2nd_endpoint.entity not in path:
                result, remaining = DFS(graph, v2nd_endpoint, search_depth-1, target, drawing_path+1)
                print(sep*drawing_depth +f'Returning to vertex: {vertex}')
                if result is not None:
                    return result, True
                elif remaining:
                    any_remaining = True  
        path.pop()
        return None, any_remaining
if __name__ == '__main__':
    g = graph.Graph()
    for i in range(10):
        g.add_vertex(i)
    vertices = {k.entity():k for k in g.vertices()} # k.entity corresponds to vertex value and k – to vertex object
    g.add_edge(vertices[0], vertices[1])
    g.add_edge(vertices[0], vertices[2])
    g.add_edge(vertices[0], vertices[4])
    g.add_edge(vertices[0], vertices[5])
    g.add_edge(vertices[4], vertices[3])
    g.add_edge(vertices[3], vertices[5])
    g.add_edge(vertices[2], vertices[6])
    path = []
    IDDFS(g, vertices[4], vertices[5])