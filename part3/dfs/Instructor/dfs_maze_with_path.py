maze = [
        [0,1,0,0],
        [0,1,0,1],
        [0,0,0,0],
        [1,1,1,0]]
        
start = (0,0)
end = (3,2)

visited = {}
visited[start] = True

directions = [(-1,0),(1,0),(0,-1),(0,1)]

# The recursion's parameter is path instead of individual point
def dfs_search(path):
    print("Current Path")
    current_row,current_column = path[-1]
    if (current_row,current_column) == end:
        return True

    for drow,dcolumn in directions:
        new_row = current_row + drow
        new_column = current_column + dcolumn
        if (new_row >= 0 and new_row < len(maze)) and \
            (new_column >= 0 and new_column < len(maze[0])):
                if maze[new_row][new_column] == 0:
                    if (new_row,new_column) not in visited:
                        visited[(new_row,new_column)] = True
                        if dfs_search(path+[(new_row,new_column)]):
                            return True
                            
    return False
    
print(dfs_search([start]))


# v2 Entry-marking DFS
def dfs_maze(current, dest, visited, path, maze):
    if current == dest:
        print("Found a path:", list(path.keys()) + [current])
        return True

    if current in visited:
        return False

    visited[current] = True
    path[current] = True

    row, col = current
    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(maze) and 0 <= nc < len(maze[0]):
            if maze[nr][nc] == 0:
                if dfs_maze((nr, nc), dest, visited, path, maze):
                    return True

    del path[current]     # backtrack
    return False


dfs_maze((0, 0), (3,3), {}, {}, maze)
