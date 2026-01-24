# version 1 - DFS add visited first - recommended
adj_list = {    
    0: [1, 3, 5], 
    1: [0, 2, 3], 
    2: [1],    
    3: [0, 1, 4, 5], 
    4: [3, 5], 
    5: [0, 3, 4]
}


def dfs(node, visited, parent):
    visited[node] = True
    
    neighbors = adj_list[node]
    
    for neighbor in neighbors:
        if neighbor in visited:
            if neighbor != parent:
                print("Cycle is detected at node",node,"for neighbor",neighbor,"parent",parent)
                return True
        else:     
            if dfs(neighbor, visited, node):
                return True
                
    return False
    
has_cycle = False
visited = {}
for node in adj_list:
    if node not in visited:
        if dfs(node, visited, -1):
            has_cycle = True
            break
            
print(has_cycle)


# version 2 - not recommended
adj_list = {
    0: [1, 3, 5],
    1: [0, 2, 3],
    2: [1],
    3: [0, 1, 4, 5],
    4: [3, 5],
    5: [0, 3, 4]
}

def getNeighbors(node):
    return adj_list[node]

def dfs(node, parent, visited):

    neighbors = getNeighbors(node)

    for neighbor in neighbors:
        # check if neighbor is visited and if it is the parent
        # if it is not the parent, then cycle is detected
        if neighbor in visited and parent != neighbor:
            print("Cycle detected: neighbor",neighbor,"parent",parent,"current node",node)
            # early break
            return True

        if neighbor not in visited:
            visited[neighbor] = True
            # early break
            if dfs(neighbor, node, visited):
                return True

    return False

visited = {}

visited[0] = True

# Caller-marking DFS becomes awkward and error-prone when you need to run DFS for all nodes (disconnected graphs).
# It is discouraged
#for node in adj_list:
#    if node not in visited:
#        visited[node] = True
#        if dfs(node, -1, visited):
#            has_cycle = True
#            break

has_cycle = dfs(0, -1, visited)
