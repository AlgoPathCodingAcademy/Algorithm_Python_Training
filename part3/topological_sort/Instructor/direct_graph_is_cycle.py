adj_list = {
    0: [1, 3, 5],
    1: [2, 3],
    2: [],
    3: [4],
    4: [5],
    5: [3]
}

# V1
def dfs(node, adj_list, visited, path):
    # entry-marking
    visited[node] = True
    path[node] = True

    for neighbor in adj_list[node]:
        if neighbor not in visited:
            if dfs(neighbor, adj_list, visited, path):
                return True
        elif neighbor in path:
            # visited + still in path ⇒ cycle
            return True

    # exit-marking
    del path[node]
    return False


visited = {}
path = {}
has_cycle = False

for node in adj_list:
    if node not in visited:
        if dfs(node, adj_list, visited, path):
            has_cycle = True
            break

print(has_cycle)

