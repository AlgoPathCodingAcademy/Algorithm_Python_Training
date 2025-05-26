nums = [1,2,3]

results = []
def permutation(path, level):
    if level == len(nums):
        results.append(path)
    for i in range(len(nums)):
        if nums[i] not in path:
            permutation(path+[nums[i]],level+1)
    
permutation([],0)

print(results)
