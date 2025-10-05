memo = {}

def getNeighbors(row, col, triangle):
    """
    Use direction vectors to find valid neighbors:
    down-left (1, -1) and down-right (1, 1)
    """
    directions = [(1, -1), (1, 1)]
    neighbors = []

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(triangle) and 0 <= nc < len(triangle[nr]):
            if triangle[nr][nc] is not None:
                neighbors.append((nr, nc))
    return neighbors


def dfs(path, triangle):
    global memo
    """
    DFS returns the minimum path sum from current node to bottom.
    path: list of (row, col) coordinates representing the current traversal.
    """

    r, c = path[-1]
    
    if (r,c) in memo:
        print("Hit Memo at",(r,c))
        return memo[(r,c)]
        
    current_val = triangle[r][c]

    # Base case: reached bottom row
    if r == len(triangle) - 1:
        print("path", path)
        return current_val

    # Recursive case: explore both neighbors and return current + min(subpaths)
    neighbor_sums = []
    for nr, nc in getNeighbors(r, c, triangle):
        neighbor_sums.append(dfs(path + [(nr, nc)], triangle))

    memo[(r,c)] = current_val + min(neighbor_sums)
    return current_val + min(neighbor_sums)


def minimum_total(triangle):
    global memo
    """
    Main function: find minimum path sum from top to bottom.
    """
    # Find starting position (top non-None value)
    memo = {}
    start = None
    for j, val in enumerate(triangle[0]):
        if val is not None:
            start = (0, j)
            break

    return dfs([start], triangle)


# Example 1
triangle1 = [
 [None, None, None,  2,  None, None, None],
 [None, None,  3,  None,  4,  None, None],
 [None,  6,  None,  5,  None,  7,  None],
 [  4,  None,  1,  None,  8,  None,  3]
]

# Example 2
triangle2 = [
 [None, None, None,  2,  None, None, None],
 [None, None,  3,  None,  2,  None, None],
 [None,  6,  None,  5,  None,  7,  None],
 [  4,  None,  4,  None,  8,  None,  1]
]

print("Example 1 Minimum Path Sum:", minimum_total(triangle1))  # Expected 11 (2→3→5→1)
#print("Example 2 Minimum Path Sum:", minimum_total(triangle2))  # Expected 12 (2→2→5→3)
