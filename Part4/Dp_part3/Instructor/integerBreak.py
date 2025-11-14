n = 4

dp = [float("-inf")] * (n+1)

dp[1] = 1

for i in range(2,n+1):
    for j in range(1,i):
        if i - j <= 0:
            continue
        dp[i] = max(dp[i],max(dp[i-j] * j, (i-j) * j))

#print(dp)
print(dp[n])
# i - 1
# i - 2
# i - (i-1) = 1
