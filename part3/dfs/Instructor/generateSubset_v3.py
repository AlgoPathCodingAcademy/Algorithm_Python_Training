nums = [1,2,3]

results = []

def generateSubSet(startIndex,path):
    results.append(path)
    for i in range(startIndex+1,len(nums)):
        generateSubSet(i,path + [nums[i]])
        
generateSubSet(-1,[])

print(results)
