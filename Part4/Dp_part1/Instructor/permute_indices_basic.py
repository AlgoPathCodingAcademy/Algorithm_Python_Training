# getNeighbors return index instead of the actual element 
items = [1,2,3]

# Note: The neighbors are nothing to do with the current node,
# which is the reason why we don't use path[-1]
def getNeighbors(path, visited,items):
    neighbors = []
    #current = path[-1]
    for i in range(len(items)):
        if i not in visited:
            neighbors.append(i)
    
    return neighbors

def dfs(path, items, visited):
    #if len(path) == len(items):
    print("Path",path)
    
    neighbors = getNeighbors(path,visited,items)
    for i in neighbors:
        visited[i] = True
        dfs(path + [items[i]], items, visited)
        del visited[i]
        

path = []
visited = {}

dfs(path, items, visited)
