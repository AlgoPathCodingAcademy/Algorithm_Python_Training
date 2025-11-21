nums = [1,2,4]
target = 4

dp = [0] * (target + 1)

dp[0] = 1

for i in range(1,target+1):
    for num in nums:
        if i >= num:
            dp[i] += dp[i - num]
        
print(dp)
