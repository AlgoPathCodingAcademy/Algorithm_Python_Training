'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
'''

def minimumObstacles(grid):
    import heapq
    start = (0,0)

    to_do_list = []
    heapq.heappush(to_do_list, (0, start))

    distance = {}
    # set all distance to inf("float")

    for row in range(len(grid)):
        for column in range(len(grid[0])):
            distance[(row,column)] = float("inf")

    distance[(0,0)] = 0

    visited = {}
    visited[start] = True

    nums_of_obstacles = 0

    directions = [(-1,0),(1,0),(0,1),(0,-1)]

    while True:
        if len(to_do_list) == 0:
            break

        current = heapq.heappop(to_do_list)
        weight, position = current
        if position == (len(grid)-1,len(grid[0])-1):
            break
        row, column = position
        visited[position] = True

        for drow,dcolumn in directions:
            new_row = row + drow
            new_column = column + dcolumn
            if new_row >= 0 and new_row < len(grid) and \
                new_column >= 0 and new_column < len(grid[0]):
                if (new_row,new_column) not in visited:
                    # relax
                    weight = 0
                    if grid[new_row][new_column] == 1:
                        weight = 1
                    else:
                        weight = 0

                    if distance[(row,column)] + weight < distance[(new_row,new_column)]:
                        distance[(new_row,new_column)] = distance[(row,column)] + weight
                        heapq.heappush(to_do_list, (distance[(new_row,new_column)], (new_row,new_column)))
						
						
    return distance[(len(grid)-1,len(grid[0])-1)]

# ----------------------------
# Test Cases Code
# ----------------------------
def run_tests():
    # Each test case is a tuple: (grid, expected_output)
    tests = [
        # Test Case 1: Single-cell grid.
        (
            [[0]],
            0
        ),
        # Test Case 2: 2x2 grid with no obstacles.
        (
            [
                [0, 0],
                [0, 0]
            ],
            0
        ),
        # Test Case 3: 2x2 grid requiring one obstacle removal.
        (
            [
                [0, 1],
                [1, 0]
            ],
            1
        ),
        # Test Case 4: 3x3 grid with a single obstacle on the best path.
        (
            [
                [0, 1, 0],
                [1, 1, 0],
                [0, 0, 0]
            ],
            1
        ),
        # Test Case 5: 3x3 grid with many obstacles.
        (
            [
                [0, 1, 1],
                [1, 1, 1],
                [1, 1, 0]
            ],
            3
        ),
        # Test Case 6: 7x7 grid (sample test case).
        (
            [
                [0,1,0,1,0,0,0],
                [0,1,1,1,0,1,0],
                [0,1,0,0,0,1,0],
                [1,1,1,1,0,1,0],
                [0,1,1,0,0,1,0],
                [0,0,1,0,0,1,0],
                [1,1,1,0,0,0,0]
            ],
            1
        ),
        # Test Case 7: 4x4 grid with all zeros.
        (
            [
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0],
                [0,0,0,0]
            ],
            0
        )
    ]
    
    all_passed = True
    for idx, (grid, expected) in enumerate(tests, start=1):
        result = minimumObstacles(grid)
        if result == expected:
            print(f"Test Case {idx}: PASS (Expected: {expected}, Got: {result})")
        else:
            print(f"Test Case {idx}: FAIL (Expected: {expected}, Got: {result})")
            all_passed = False

    if all_passed:
        print("\nAll test cases passed!")
    else:
        print("\nSome test cases failed.")


run_tests()
