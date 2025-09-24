def getNeighbors(used, items):
    neigh = []
    for i in range(len(items)):
        if i in used:
            continue
        # classic duplicate-skip rule
        if i > 0 and items[i] == items[i - 1] and (i - 1) not in used:
            continue
        neigh.append(i)
    return neigh
    
def show(used, items):
    neigh = getNeighbors(used, items)
    chars = [items[i] for i in neigh]
    print(f"used={list(used.keys())} -> neighbors {neigh} -> chars {chars}")

items = [1,2,2]

used = {}
show(used,items)

used = {0:True}
show(used,items)

used = {0:True, 1:True}
show(used,items)

def dfs(path, items, visited):
    if len(path) == len(items):
        print("Show Path", path)
        return

    neighbors = getNeighbors(visited, items)
    for neighbor in neighbors:
        visited[neighbor] = True
        dfs(path + [items[neighbor]], items,visited)
        del visited[neighbor]
        
dfs([],items,{})
