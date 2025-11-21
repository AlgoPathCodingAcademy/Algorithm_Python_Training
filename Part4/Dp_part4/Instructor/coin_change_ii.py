nums = [1,2,5]
target = 5

dp = [0] * (target + 1)

dp[0] = 1

for num in nums:
    for i in range(1,target+1):
        if i >= num:
            dp[i] += dp[i - num]
        
print(dp)
