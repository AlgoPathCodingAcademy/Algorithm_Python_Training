items = [1,2,3]

# Note: The neighbors are nothing to do with the current node,
# which is the reason why we don't use path[-1]
def getNeighbors(path, visited,items):
    neighbors = []
    #current = path[-1]
    for item in items:
        if item not in visited:
            neighbors.append(item)
    
    return neighbors
    
path = []
visited = {}
print(getNeighbors(path, visited, items))

#path = []
visited = {1:True}
print(getNeighbors(path, visited, items))

visited = {1:True,2:True}
print(getNeighbors(path, visited, items))


def dfs(path, items, visited):
    #if len(path) == len(items):
    print("Path",path)
    
    neighbors = getNeighbors(path,visited,items)
    for neighbor in neighbors:
        visited[neighbor] = True
        dfs(path + [neighbor], items, visited)
        del visited[neighbor]
        

path = []
visited = {}

dfs(path, items, visited)
