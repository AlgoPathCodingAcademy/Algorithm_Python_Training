def knight_left_to_right_dp(maze):
    rows = len(maze)
    columns = len(maze[0])

    dp = [[float("inf")] * columns for _ in range(rows)]
    dp[0][0] = 0

    directions = [(-1, 2), (1, 2), (-2, 1), (2, 1)]

    for column in range(columns):
        for row in range(rows):

            if dp[row][column] == float("inf"):
                continue

            if maze[row][column] == 1:
                continue

            for drow, dcolumn in directions:
                nr = row + drow
                nc = column + dcolumn

                if 0 <= nr < rows and 0 <= nc < columns:
                    if maze[nr][nc] == 0:
                        dp[nr][nc] = min(dp[nr][nc], dp[row][column] + 1)

    return dp
    
def print_dp(dp):
    for row in dp:
        print(row)
    print()



from collections import deque

def bfs_ground_truth(maze, dest):
    rows = len(maze)
    cols = len(maze[0])
    dr, dc = dest

    if maze[0][0] == 1 or maze[dr][dc] == 1:
        return -1

    moves = [(-1,2),(1,2),(-2,1),(2,1)]
    q = deque([(0,0,0)])  # (r,c,dist)
    visited = set([(0,0)])

    while q:
        r,c,d = q.popleft()
        if (r,c) == (dr,dc):
            return d

        for dr0,dc0 in moves:
            nr,nc = r+dr0, c+dc0
            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 0:
                    if (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc,d+1))

    return -1

def run_test(maze, dest, name):
    print(f"=== {name} ===")
    dp = knight_left_to_right_dp(maze)
    dr, dc = dest

    dp_ans = dp[dr][dc] if dp[dr][dc] != float("inf") else -1
    bfs_ans = bfs_ground_truth(maze, dest)

    print("DP table:")
    for row in dp: print(row)
    print(f"DP result = {dp_ans}")
    print(f"BFS ground truth = {bfs_ans}")

    if dp_ans == bfs_ans:
        print("→ PASS ✓\n")
    else:
        print("→ FAIL ✗\n")
    
# ------------------------
# RUNNING ALL TEST CASES
# ------------------------

tests = [

    # Your original
    ([[0,1,0],
      [0,0,1],
      [0,0,0]],
     (2,2),
     "Test A: Original 3×3, target (2,2)"),

    # Completely empty grid
    ([[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     (1,3),
     "Test B: Empty 3×4, target (1,3)"),

    # Blocking first column
    ([[0,1,0],
      [0,1,0],
      [0,0,0]],
     (2,2),
     "Test C: Blocked mid column, target (2,2)"),

    # Completely blocked middle row (unreachable)
    ([[0,0,0],
      [1,1,1],
      [0,0,0]],
     (2,2),
     "Test D: Destination unreachable"),

    # Larger tricky case (row-first fails)
    ([[0,0,0,0,0],
      [0,1,0,1,0],
      [0,0,0,0,0],
      [0,0,1,0,0]],
     (3,4),
     "Test E: Row-first fails but column-first correct, target (3,4)"),

    # 4×4 test for deeper jumps
    ([[0,0,0,0],
      [0,0,0,0],
      [0,0,0,0],
      [0,0,0,0]],
     (2,3),
     "Test F: Open board, target (2,3)")
]

for maze, dest, name in tests:
    run_test(maze, dest, name)
