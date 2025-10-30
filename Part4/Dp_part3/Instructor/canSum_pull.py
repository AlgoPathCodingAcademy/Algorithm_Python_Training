nums = [5,3,4,7]
#nums = [2,3]
target = 7

dp = [False] * (target+1)
dp[0] = True
def canSum(nums, target):
    for i in range(1,target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] = dp[i] or dp[i-num]
            
    print(dp)
    return dp[target]
        
print(canSum(nums,target))

# Early Break Version - (Slight improvement)
def canSum_pull_optimized(nums, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0 and dp[i - num]:
                dp[i] = True
                break  # no need to check more numbers
    return dp[target]
