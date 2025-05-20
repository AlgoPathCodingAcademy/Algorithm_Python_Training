nums = [1,2,3]
result = []

def generateSubset(path,level):
    if level == len(nums):
        result.append(path)
        return

    generateSubset(path,level+1)
    generateSubset(path + [nums[level]],level+1)
    
generateSubset([],0)

print(result)
