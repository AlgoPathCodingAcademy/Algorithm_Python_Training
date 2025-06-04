lst = [1,2,3]
results = []

def permutation(path,nums,visited,results):
    if len(path) == len(nums):
        results.append(path)
        return
    
    for i in range(len(nums)):
        if i not in visited:
            visited[i] = True
            permutation(path + [nums[i]],nums,visited,results)
            del visited[i]
        
permutation([],lst,{},results) 

print(results)
