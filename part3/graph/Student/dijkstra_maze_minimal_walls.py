'''
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).
'''

from collections import deque

def minimumObstacles(grid):








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
