def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    
    for row in range(m):
        for column in range(n):
            if row == 0:
                dp[row][column] = 1
            elif column == 0:
                dp[row][column] = 1
            else:
                dp[row][column] = dp[row-1][column] + dp[row][column-1]
    
    return dp[m-1][n-1]
