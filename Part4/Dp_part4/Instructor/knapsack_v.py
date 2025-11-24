weights = [1, 2, 3, 3,7]
capacity = 7

dp = [[0]*(capacity+1) for _ in range(len(weights) + 1)]

for i in range(len(weights) + 1):
    dp[i][0] = 1

for i in range(1, len(weights) + 1):
    for w in range(1, capacity+1):

        # The original formular is
        # dp[i][w] = dp[i-1][w] + dp[i-1][w-weights[i-1]]

        if w < weights[i-1]:
            dp[i][w] = dp[i-1][w]
        if w >= weights[i-1]:
            dp[i][w] =  dp[i-1][w] + dp[i-1][w-weights[i-1]]

            
print(dp)
