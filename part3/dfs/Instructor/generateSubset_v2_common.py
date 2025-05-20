nums = [1,2,3]

results = []

def generateSubSet(path):
    results.append(path)    
    for i in range(len(nums)):
        if path and path[-1] >= nums[i]:
            continue
        generateSubSet(path + [nums[i]])
        
generateSubSet([])

print(results)
