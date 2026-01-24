edges = [(5,2),(5,0),(4,0),(4,1),(2,3),(3,1)]
#edges = [(1,5),(2,3),(3,5)]
#edges = [("A","D"),("B","C"),("C","D")]
adj_list = {}

for u,v in edges:
    if u not in adj_list:
        adj_list[u] = [v]
    else:
        adj_list[u].append(v)

# The numbers of node would normally be provided by the question
# In our test case, it is 6.
for node in range(6):
    if node not in adj_list:
        adj_list[node] = []
        
print(adj_list)


def dfs(graph, node,visited,result):
    visited[node] = True
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph,neighbor,visited,result)
            
    result.append(node)
    
    
visited = {}
result = []
for node in adj_list:
    if node not in visited:
        dfs(adj_list, node,visited,result)
        
print(result[::-1])
    
