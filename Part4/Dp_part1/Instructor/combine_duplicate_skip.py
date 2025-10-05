items = [1,2,2]

def getNeighbors(index,items):
    neighbors = []
    start = index + 1
    for i in range(len(items)):
        if i > start and items[i] == items[i-1]:
            continue

        if i > index:
            neighbors.append(i)
        
    return neighbors

visited = {}

print(getNeighbors(-1,items))

print(getNeighbors(0,items))

print(getNeighbors(1,items))


def dfs(index, path, items):
    print("Path",path)
    neighbors = getNeighbors(index, items)
    for neighbor in neighbors:
        dfs(neighbor, path + [items[neighbor]], items)
        
dfs(-1,[],items)
