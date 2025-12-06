def getNeighbors(visited,nums):
    neighbors = []
    for i in range(len(nums)):
        if i >= 1 and nums[i-1] == nums[i] and i-1 not in visited:
            continue
        
        if i not in visited:
            neighbors.append(i)
            
    return neighbors
    
    
def dfs(path, visited, nums):
    if len(path) == len(nums):
        print(path)
        
    neighbors = getNeighbors(visited, nums) 
    
    for neighbor in neighbors:
        visited[neighbor] = True
        dfs(path + [nums[neighbor]],visited, nums)
        del visited[neighbor]
        
        
nums = [7,9,9]
dfs([], {}, nums)
