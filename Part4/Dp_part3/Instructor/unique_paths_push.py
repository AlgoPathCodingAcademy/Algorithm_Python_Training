# In Push DP, one state can be updated multiple times.
# In Pull DP, each state is updated exactly once.
def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for row in range(m):
        for col in range(n):
            if col + 1 < n:
                dp[row][col + 1] += dp[row][col]  # push right
            if row + 1 < m:
                dp[row + 1][col] += dp[row][col]  # push down
    return dp[m - 1][n - 1]
