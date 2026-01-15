edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
#edges = [(1,5),(2,3),(3,5)]
#edges = [("A","D"),("B","C"),("C","D")]
adj_list = {}

for u,v in edges:
    if u not in adj_list:
        adj_list[u] = [v]
    else:
        adj_list[u].append(v)
        

print(adj_list)


#adj_list = {
#    'A': ['C'],
#    'B': ['C', 'D'],
#    'C': ['D'],
#    'D': ['E'],
#    'E': []
#}

def getNeighbors(current):
    if current not in adj_list:
        return []
        
    return adj_list[current]
    
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
