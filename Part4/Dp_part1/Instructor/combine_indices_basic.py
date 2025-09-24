items = [1,2,3]

def getNeighbors(index, items):
    neighbors = []
    
    for i in range(len(items)):
        if i > index:
            neighbors.append(i)
            
    return neighbors
    
    
def dfs(index, path,items):
    print("path",path)
    neighbors = getNeighbors(index, items)
    for i in neighbors:
        dfs(i, path + [items[i]], items)
        
        
dfs(-1,[],items)
