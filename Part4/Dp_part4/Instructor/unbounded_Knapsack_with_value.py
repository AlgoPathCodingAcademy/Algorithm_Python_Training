weight = [2,3,4]
value = [3,7,10]

cap = 10

dp = [0] * (cap + 1)

for i in range(cap + 1):
    for j in range(len(weight)):
        if i - weight[j] < 0:
            continue
        dp[i] = max(dp[i-weight[j]] + value[j], dp[i])

print(dp)
