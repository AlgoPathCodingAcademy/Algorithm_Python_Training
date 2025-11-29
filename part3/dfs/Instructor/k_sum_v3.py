nums = [1,2,3,4]
k = 2
target = 5

def getNeighbors(current, nums,level):
    neighbors = []
    
    for num in nums:
        if current != None and current <= num:
            continue
        neighbors.append(num)
        
    return neighbors

def dfs(total_sum, path, current, nums, level, k, target):
    if total_sum > target:
        return
    
    if total_sum == target:
        print("Sum", path)
        return
    
    if level == k:
        return
    
    neighbors = getNeighbors(current, nums,level)
    for neighbor in neighbors:
        dfs(total_sum + neighbor, path + [neighbor], neighbor, nums, level+1, k, target)
        

dfs(0,[],None,nums,0, k,target)
