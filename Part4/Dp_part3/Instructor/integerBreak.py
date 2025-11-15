n = 4

dp = [float("-inf")] * (n+1)
print(dp)

dp[2] = 1

for i in range(3,n+1):
    for j in range(1,i):
        if i - j < 2:
            continue

        dp[i] = max(dp[i-j] * j, (i-j)*j,dp[i])

print(dp)
