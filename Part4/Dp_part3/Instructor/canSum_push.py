nums = [5,3,4,7]
#nums = [2,3]
target = 7
dp = [False] * (target + 1)
dp[0] = True
def canSum(nums, target):
    for i in range(0, target+1):
        for num in nums:
            if i + num <= target:
                dp[i+num] = dp[i+num] or dp[i]
                
    print(dp)
    return dp[target]
    
print(canSum(nums,target))

def canSum_optimized(nums, target):
    for i in range(0, target+1):
        for num in nums:
            if i + num <= target and dp[i]:
                dp[i+num] = True
                
    print(dp)
    return dp[target]
    
print(canSum_optimized(nums,target))
