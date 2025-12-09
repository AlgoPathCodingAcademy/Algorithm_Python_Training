def unique_paths(m, n):
    dp = [[0] * n for _ in range(m)]
    parent = [[(-1,-1)] * n for _ in range(m)]
    
    for row in range(m):
        for column in range(n):
            if row == 0:
                dp[row][column] = 1
                parent[row][column] = (row,column-1)
            elif column == 0:
                dp[row][column] = 1
                parent[row][column] = (row-1,column)
            else:
                dp[row][column] = dp[row-1][column] + dp[row][column-1]
                
                parent[row][column] = (row-1,column)
                    
    # Reconstruct path
    path = []
    current_row,current_column = m-1, n-1
    path.append((current_row,current_column))
    while True:
        prev_row,prev_column = parent[current_row][current_column]
        
        if prev_row == -1 or prev_column == -1:
            break
        
        path.append((prev_row,prev_column))
        
        current_row = prev_row
        current_column = prev_column
    
    print("One Path", path[::-1])
    
    return dp[m-1][n-1]

row = 3
column = 3
print(unique_paths(row,column))
