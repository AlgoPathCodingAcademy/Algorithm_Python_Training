# version 1 - DFS add visited first
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

def dfs_v2(node, visited, parent):
    visited[node] = True
    neighbors = getNeighbors(node)
    
    for neighbor in neighbors:
        if neighbor in visited and neighbor != parent:
            print("Cycle detected: neighbor", neighbor, "parent",parent, "node",node)
            return True
            
        if neighbor not in visited:
            if dfs_v2(neighbor,visited,node):
                return True

    return False
    
visited = {}
print(dfs_v2(0,visited,-1))


# version 2:
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

has_cycle = dfs(0, -1, visited)
