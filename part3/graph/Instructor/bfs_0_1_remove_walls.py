from collections import deque

def minimumObstacles(grid):
    start = (0,0)
    to_do_list = deque()
    to_do_list.append(start)

    rows = len(grid)
    columns = len(grid[0])

    end = (rows-1, columns-1)

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    path = {}

    for i in range(rows):
        for j in range(columns):
            path[(i,j)] = float("inf")

    path[start] = 0

    while True:
        row,column = to_do_list.popleft()

        if (row,column) == end:
            break

        for drow, dcolumn in directions:
            new_row = row + drow
            new_column = column + dcolumn
            if (new_row >= 0 and new_row < rows) and \
                (new_column >= 0 and new_column < columns):
                    
                cost = grid[new_row][new_column]
                if path[(row,column)] + cost < path[(new_row,new_column)]:
                    path[(new_row,new_column)] = path[(row,column)] + cost
                    if grid[new_row][new_column] == 1:
                        to_do_list.append((new_row,new_column))
                    else:
                        to_do_list.appendleft((new_row,new_column))

    return path[end]
    
print(minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
print(minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))
