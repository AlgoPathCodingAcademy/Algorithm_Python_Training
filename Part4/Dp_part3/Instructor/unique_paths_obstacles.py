#obstacle_grid = [[0]]
#obstacle_grid = [[0,0,0],[0,1,0],[0,0,0]]
#obstacle_grid = [[0,0,0],[1,0,0],[0,0,0]]
obstacle_grid = [[0,1,0],[0,0,0],[0,0,0]]

dp = [ [0] * len(obstacle_grid[0]) for _ in range(len(obstacle_grid))]

rows = len(obstacle_grid)
columns = len(obstacle_grid[0])

for row in range(rows):
    for column in range(columns):
        dp[0][column] = 1
        dp[row][0] = 1


for row in range(rows):
    for column in range(columns):
        if row == 0 and obstacle_grid[row][column] == 1:
            for i in range(column,columns):
                dp[0][i] = 0

        if column == 0 and obstacle_grid[row][column] == 1:
            for j in range(row,rows):
                dp[j][0] = 0


for row in range(1, rows):
    for column in range(1, columns):
        if obstacle_grid[row][column] == 1:
            dp[row][column] = 0
            continue

        dp[row][column] = dp[row][column-1] + dp[row-1][column]

print(dp[rows-1][columns-1])
