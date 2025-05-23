nums = [1,2,2]

results = []

def generateSubSet(startIndex,path):
    results.append(path)
    for i in range(startIndex+1,len(nums)):
        if i > startIndex+1 and nums[i] == nums[i-1]:
            continue
        generateSubSet(i,path + [nums[i]])
        
generateSubSet(-1,[])

print(results)
