edge_list = [[1,2],[1,3],[2,4],[3,4],[3,5],[6,7]]
nodes = 8
adj_list = {}
for node in range(nodes):
    adj_list[node] = []
    
for u,v in edge_list:
    adj_list[u].append(v)
    adj_list[v].append(u)
    
print(adj_list)
