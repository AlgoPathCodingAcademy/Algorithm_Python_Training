nums = [5,1,2,3,0]

dp = [1] * len(nums)

for i in range(1,len(nums)):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j] + 1, dp[i])

max_length = max(dp)
print(dp)
print("max length",max_length)
