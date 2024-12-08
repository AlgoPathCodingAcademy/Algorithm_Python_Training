def find_equilibrium_index(arr):
    """
    Find an equilibrium index in the array where the sum of elements on the left
    equals the sum of elements on the right.

    :param arr: List[int] - The input array
    :return: int - The equilibrium index or -1 if no such index exists
    """
    #TODO

def test_find_equilibrium_index():
    test_cases = [
        ([3, 4, 8, -9, 20, 6], 4),  # Example 1
        ([1, 2, 3, 4, 6], 3),      # Example 2
        ([1, -1, 4], 2),            # Example 3
        ([0], 0),                   # Example 4
        ([1, 1, -1, 1, -1, 1, -1], 0),  # Custom case
        ([1, -1, 1, -1, -1, 1, 9], 6),  # Custom case
        ([2, 3, -1, 8, 4, -2, 3], -1),  # Custom case
        ([], -1),                   # Empty array case
        ([1], 0),                   # Single element case
    ]
    
    for i, (arr, expected) in enumerate(test_cases):
        result = find_equilibrium_index(arr)
        if result == expected:
            print(f"Test Case {i + 1}: Passed")
        else:
            print(f"Test Case {i + 1}: Failed (Expected {expected}, Got {result})")

# Run tests
test_find_equilibrium_index()
