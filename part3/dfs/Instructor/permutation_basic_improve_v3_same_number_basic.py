def getNeighbors(visited, lst):
    neighbors = []
    for i in range(len(lst)):
        if i not in visited:
            neighbors.append(i)
    return neighbors


def dfs(visited, lst, path):
    if len(path) == len(lst):
        print(path)
        return

    neighbors = getNeighbors(visited, lst)

    for neighbor in neighbors:
        visited[neighbor] = True
        dfs(visited, lst, path + [lst[neighbor]])
        del visited[neighbor]


nums = [1, 2, 2]
visited = {}
path = []

dfs(visited, nums, path)
