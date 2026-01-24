def dfs(node, visited, visiting):
    # mark entry
    visiting.add(node)

    for neighbor in adj_list.get(node, []):
        # Case 1: back edge → cycle
        if neighbor in visiting:
            return True

        # Case 2: tree edge → recurse
        if neighbor not in visited:
            if dfs(neighbor, visited, visiting):
                return True

    # mark exit
    visiting.remove(node)
    visited.add(node)
    return False


visited = set()
visiting = set()
has_cycle = False

for node in adj_list:
    if node not in visited:
        if dfs(node, visited, visiting):
            has_cycle = True
            break

print(has_cycle)


adj_list = {
    0: [1, 3, 5],
    1: [2, 3],
    2: [],
    3: [4],
    4: [5],
    5: [3]
}

def dfs(node,visited,path):
    if node in path:
        print("cycle detected", node, "in",path)
        return True
    
    if node in visited:
        return False
    
    visited[node] = True
    path[node] = True
    
    neighbors = adj_list[node]
    
    for neighbor in neighbors:
        if dfs(neighbor,visited,path):
            return True
    
    del path[node]
        
    return False
        
visited = {}
path = {}
for key in adj_list:
    if key not in visited:
        if dfs(key,visited,path):
            break 


# v2 verison 
adj_list = {
    0: [1, 3, 5],
    1: [2, 3],
    2: [],
    3: [4],
    4: [5],
    5: [3]
}

def dfs_v2(node,path,visited):
    for neighbor in adj_list[node]:
        if neighbor in path:
            print("Cycle Detected", "neighbor",neighbor,"in path",path)
            return True

        if neighbor not in visited:
            path[neighbor] = True
            visited[neighbor] = True
            if dfs_v2(neighbor,path,visited):
                return True
            del path[neighbor]

    return False


visited = {}
path = {}
for key in adj_list:
    if key not in visited:
        visited[key] = True
        path[key] = True
        if dfs_v2(key,path,visited):
            break
        del path[key]



