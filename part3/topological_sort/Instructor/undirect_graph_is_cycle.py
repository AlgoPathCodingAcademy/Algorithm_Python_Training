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
        if neighbor in visited and parent[node] != neighbor:
            print("neighbor",neighbor,"parent",parent[node],"current node",node)
            print("cycle is detected")
            # early break
            return True

        if neighbor not in visited:
            visited[neighbor] = True
            parent[neighbor] = node
            # early break
            if dfs(neighbor, parent, visited):
                return True
                
    return False
    
visited = {}

visited[0] = True

parent = {}
parent[0] = -1

has_cycle = dfs(0, parent, visited)



# version 2 - DFS add visited first
adj_list = {
    0: [1, 3, 5],
    1: [0, 2, 3],
    2: [1],
    3: [0, 1, 4, 5],
    4: [3, 5],
    5: [0, 3, 4]
}

def dfs_v2(node, parent, visited):
    visited.add(node)

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if dfs_v2(neighbor, node, visited):
                return True
        elif neighbor != parent:
            return True

    return False

visited = set()

has_cycle = dfs_v2(0, -1, visited)

