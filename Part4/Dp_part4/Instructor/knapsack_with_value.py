weights = [1,3,4,5]
value = [15,20,30,50]
capacity = 7

dp = [[0]*(capacity + 1) for _ in range(len(value) + 1)]

for v in range(1, len(value) + 1):
    for c in range(1, capacity + 1):

        if c < weights[v-1]:
            dp[v][c] = dp[v-1][c]
        else:
            dp[v][c] = max(dp[v-1][c-weights[v-1]] + value[v-1], dp[v-1][c])
            
print(dp)
