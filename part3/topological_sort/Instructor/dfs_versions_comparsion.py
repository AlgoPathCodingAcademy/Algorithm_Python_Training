## version 1 ##
def dfs(graph, node,visited,result):
    
    visited[node] = True
    
    neighbors = graph[node]
    
    for neighbor in neighbors:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
            
    result.append(node)

def topo_sort(graph):
    """
    graph: dict {node: [neighbors]}
    returns: list representing a topological order
    Assumes graph is a DAG (no cycle detection)
    """
    result = []
    visited = {}
    for node in graph:
        if node not in visited:
            dfs(graph,node,visited,result)

    return result[::-1]

## version 2 ##
def dfs(graph, node,visited,result):

    if node in visited:
        return

    visited[node] = True

    neighbors = graph[node]
    for neighbor in neighbors:
        dfs(graph, neighbor, visited, result)

    result.append(node)


def topo_sort(graph):
    """
    graph: dict {node: [neighbors]}
    returns: list representing a topological order
    Assumes graph is a DAG (no cycle detection)
    """
    result = []
    visited = {}
    for node in graph:
        dfs(graph,node,visited,result)

    return result[::-1]

## version 3 ##
finished = {}
result = []

def dfs(node, visited):

    neighbors = getNeighbors(node)

    for neighbor in neighbors:
        if neighbor not in visited:
            visited[neighbor] = True
            dfs(neighbor,visited)

    if node not in finished:
        finished[node] = True
        result.append(node)

visited = {}
for key in adj_list:
    visited = {key:True}
    dfs(key,visited)

print(result[::-1])
