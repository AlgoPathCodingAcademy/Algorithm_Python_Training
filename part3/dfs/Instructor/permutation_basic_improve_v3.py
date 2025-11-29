def getNeighbors(visited, lst):
    neighbors = []
    for i in range(len(lst)):
        if lst[i] not in visited:
            neighbors.append(lst[i])
    return neighbors


def dfs(visited, lst, path):
    if len(path) == len(lst):
        print(path)
        return

    neighbors = getNeighbors(visited, lst)

    for neighbor in neighbors:
        visited[neighbor] = True
        dfs(visited, lst, path + [neighbor])
        del visited[neighbor]


nums = [1, 2, 3]
visited = {}
path = []

dfs(visited, nums, path)
