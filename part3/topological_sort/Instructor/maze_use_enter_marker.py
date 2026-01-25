# Find one Path
def dfs_maze(maze, r, c, dest, visited, path):
    # entry-mark
    visited[(r, c)] = True
    path.append((r, c))

    # reached destination
    if (r, c) == dest:
        return True

    rows, cols = len(maze), len(maze[0])
    directions = [(1,0), (-1,0), (0,1), (0,-1)]

    for dr, dc in directions:
        nr, nc = r + dr, c + dc

        if 0 <= nr < rows and 0 <= nc < cols:
            if maze[nr][nc] == 1 and (nr, nc) not in visited:
                if dfs_maze(maze, nr, nc, dest, visited, path):
                    return True

    # backtrack
    path.pop()
    return False

# Find all Paths
def dfs_all_paths(maze, r, c, dest, visited, path, all_paths):
    visited[(r, c)] = True
    path.append((r, c))

    if (r, c) == dest:
        # store a COPY of the current path
        all_paths.append(path[:])
    else:
        rows, cols = len(maze), len(maze[0])
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if maze[nr][nc] == 1 and (nr, nc) not in visited:
                    dfs_all_paths(maze, nr, nc, dest, visited, path, all_paths)

    # BACKTRACK BOTH
    path.pop()
    del visited[(r, c)]
