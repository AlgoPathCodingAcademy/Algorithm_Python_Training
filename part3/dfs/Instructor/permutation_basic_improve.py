nums = [1,2,3]

results = []
def permutation(path, level, visited):
    if level == len(nums):
        results.append(path)
    for i in range(len(nums)):
        if nums[i] not in visited:
            visited[nums[i]] = True
            permutation(path+[nums[i]],level+1, visited)
            del visited[nums[i]]
    
permutation([],0,{})

print(results)
