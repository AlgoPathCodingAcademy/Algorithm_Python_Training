def first_position(nums, target):
    if len(nums) == 0:
        return -1
        
    start = 0
    end = len(nums) - 1
    
    while True:
        if start + 1 >= end:
            break
        
        middle = (start + end)//2
        
        if nums[middle] < target:
            start = middle
        elif nums[middle] == target:
            end = middle
        else:
            end = middle
            
    if nums[start] == target:
        return start

    if nums[end] == target:
        return end
        
    return -1


# ── TEST HARNESS ─────────────────────────────────────────────────────────────
def _truth(nums, target):
    """Ground-truth using Python’s .index(); –1 if absent."""
    try:
        return nums.index(target)
    except ValueError:
        return -1


def run_tests():
    import random

    # 1. Examples + hand-picked edge cases
    cases = [
        #  description              nums                            target
        ("duplicates mid",          [1, 2, 2, 2, 3, 4],             2),
        ("all duplicates",          [1, 1, 1, 1],                   1),
        ("duplicates end",          [5, 7, 7, 8, 8, 10],            8),
        ("absent",                  [2, 4, 6, 8],                   5),
        ("empty list",              [],                             0),
        ("single hit",              [9],                            9),
        ("single miss",             [9],                           10),
        ("no dup first elem",       [1, 3, 5, 7],                   1),
        ("no dup last elem",        [1, 3, 5, 7],                   7),
        ("neg & zeros hit",         [-5, -3, -1, 0, 0, 2],          0),
        ("neg target absent",       [-4, -3, -1, 2, 4],            -2),
        ("target < min",            [3, 4, 5],                      1),
        ("target > max",            [3, 4, 5],                      9),
        ("dups at start",           [4, 4, 4, 5, 6],                4),
        ("large list tail dups",    list(range(100_000)) + [100_000]*7, 100_000),
    ]

    # 2. Five random cases for extra confidence
    for i in range(5):
        size   = random.randint(0, 1000)
        nums   = sorted(random.randint(-2000, 2000) for _ in range(size))
        target = random.choice(nums + [5000])  # ~50 % chance of “miss”
        cases.append((f"random {i+1}", nums, target))

    # 3. Run and report
    for desc, nums, target in cases:
        expected = _truth(nums, target)
        got      = first_position(nums, target)
        if got == expected:
            print(f"PASS: {desc}")
        else:
            print(f"FAIL: {desc}  → expected {expected}, got {got}")


# Run when this file is executed directly
if __name__ == "__main__":
    run_tests()
