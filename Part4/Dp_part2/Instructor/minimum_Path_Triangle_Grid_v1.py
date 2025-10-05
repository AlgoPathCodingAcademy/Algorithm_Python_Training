# Global variable to track the minimum path sum
min_sum = float("inf")

def getNeighbors(row, col, triangle):
    """
    Use direction vectors to find valid neighbors.
    Directions: (down-left), (down-right)
    """
    directions = [(1, -1), (1, 1)]  # move one row down, one column left/right
    neighbors = []

    for dr, dc in directions:
        nr, nc = row + dr, col + dc
        if 0 <= nr < len(triangle) and 0 <= nc < len(triangle[nr]):
            if triangle[nr][nc] is not None:
                neighbors.append((nr, nc))
    return neighbors

def dfs(path, triangle):
    """
    DFS traversal using path as parameter.
    """
    global min_sum
    r, c = path[-1]
    current_val = triangle[r][c]

    # Base case: reached the last row
    if r == len(triangle) - 1:
        path_sum = sum(triangle[x][y] for x, y in path)
        min_sum = min(min_sum, path_sum)
        return

    # Recursive case: explore all valid neighbors
    for nr, nc in getNeighbors(r, c, triangle):
        dfs(path + [(nr, nc)], triangle)


def minimum_total(triangle):
    """
    Main function: finds the minimum path sum in the triangle grid.
    """
    global min_sum

    min_sum = float("inf")

    # Find the top non-None starting position
    start = None
    for j, val in enumerate(triangle[0]):
        if val is not None:
            start = (0, j)
            break

    # Start DFS from the top
    dfs([start], triangle)
    return min_sum


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
print("Example 2 Minimum Path Sum:", minimum_total(triangle2))  # Expected 12 (2→2→5→3)
