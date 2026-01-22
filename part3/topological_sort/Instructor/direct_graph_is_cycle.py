def dfs_v2(node, path, visited):
    # If node is on the current recursion stack → cycle
    if node in path:
        return True

    # If node is fully processed → safe
    if node in visited:
        return False

    # Mark node as being on the current path
    path[node] = True

    for neighbor in adj_list[node]:
        if dfs_v2(neighbor, path, visited):
            print(
                "Cycle detected via edge:",
                node, "→", neighbor,
                "| path:", list(path.keys())
            )
            return True

    # Remove node from current path, mark fully processed
    del path[node]
    visited[node] = True
    return False
    
    
path = {}
visited = {}

for node in adj_list:
    if dfs_v2(node, path, visited):
        break

