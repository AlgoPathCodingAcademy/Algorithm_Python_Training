# level tracks the last processed index, not the current candidate.
lst = [1,2,3]

def getNeighbors(path, level, nums):
    neighbors = []
    current = path[-1]
    neighbors.append(current)
    neighbors.append(current + [nums[level+1]])
    return neighbors

def dfs(path,level,nums):
    if level == len(lst)-1:
        print("path",path[-1])
        return

    neighbors = getNeighbors(path, level, nums)
        
    for neighbor in neighbors:
        dfs(path+[neighbor], level + 1, nums)

dfs([[]],-1,lst)
