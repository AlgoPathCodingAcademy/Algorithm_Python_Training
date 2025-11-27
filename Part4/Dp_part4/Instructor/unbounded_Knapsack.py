weight = 11

nums = [2,3,5,7]

dp = [0] * (weight+1) 

for i in range(1,weight+1):
    for num in nums:
        if i < num:
            continue
        dp[i] = max(dp[i-num] + num, dp[i])
        
print(dp)
