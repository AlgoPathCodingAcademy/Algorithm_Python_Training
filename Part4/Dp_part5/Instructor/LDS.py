nums = [9, 4, 3, 2, 5, 4, 3, 2]
dp = [1] * len(nums)

for i in range(1, len(nums)):
    for j in range(i):
        if nums[j] > nums[i]:
            dp[i] = max(dp[j] + 1,dp[i])
            
print(dp)
print(max(dp))
