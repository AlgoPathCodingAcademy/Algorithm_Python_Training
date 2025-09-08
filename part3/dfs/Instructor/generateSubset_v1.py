nums = [1,2,3]
result = []

def generateSubset(current,level):
    if level == len(nums):
        result.append(current)
        return

    generateSubset(current,level+1)
    generateSubset(current + [nums[level]],level+1)
    
generateSubset([],0)

print(result)
