def bfs(start, maze, visited):
    from collections import deque
    visited[start] = True

    to_do_list = deque()
    to_do_list.append(start)

    visited_counter = 0

    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # Debug Purpose
    path = {}
    path[start] = None
    row = 0
    column = 0

    while True:
        if len(to_do_list) == 0:
            break

        row,column = to_do_list.popleft()
        if maze[row][column] == 1:
            visited_counter = visited_counter + 1

        for dx,dy in directions:
            new_row = dx + row
            new_column = dy + column
            if (new_row >= 0 and new_row < len(maze)) and \
                (new_column >= 0 and new_column < len(maze[0])) and \
                (maze[new_row][new_column] == 1):
                    if (new_row,new_column) not in visited:
                        to_do_list.append((new_row,new_column))
                        visited[(new_row,new_column)] = True
                        # Debug Purpose
                        path[(new_row,new_column)] = row,column

    if visited_counter > 0:
        display_path = []
        end = (row,column)
        while True:
            display_path.append(end)
            pre_path = path[end]
            end = pre_path
            if end == None:
                break
        print("Show Path",display_path)
        return True
    else:
        return False


def num_islands(grid):
    visited_hash_table = {}
    nums_island = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == 1 and (row,col) not in visited_hash_table:
                if (bfs((row,col),grid,visited_hash_table)):
                    nums_island = nums_island + 1

    return nums_island
    
maze = [
  [1,1,0,0,0],
  [0,1,0,0,1],
  [0,0,0,1,1],
  [0,0,0,0,0],
  [0,0,0,0,1]]
  
print(num_islands(maze))
