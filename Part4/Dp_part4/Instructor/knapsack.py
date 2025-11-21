iweights = [2, 3, 5, 7]
capacity = 11

dp = [[0]*(capacity+1) for _ in range(len(weights) + 1)]

# Base case but should be removed
# Just for illustration purpose
# for row in range(len(weights) + 1):
#    for column in range(capacity+1):
#        dp[0][column] = 0
#        dp[row][0] = 0

for i in range(1, len(weights) + 1):
    for w in range(1, capacity+1):
        if w < weights[i-1]:
            dp[i][w] = dp[i-1][w]
        else:
            dp[i][w] = max(dp[i-1][w-weights[i-1]] + weights[i-1], dp[i-1][w])
            
print(dp)
