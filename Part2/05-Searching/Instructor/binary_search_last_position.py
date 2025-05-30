def last_position(nums, target):
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
            start = middle
        else:
            end = middle
            
    if nums[end] == target:
        return end
        
    if nums[start] == target:
        return start

# ── test-driver ────────────────────────────────────────────────
def run_tests():
    """Run a battery of deterministic & random tests; print pass/fail."""
    import random

    # ---------- curated edge-cases ----------
    cases = [
        ("empty list",               [],                     5),
        ("one element – hit",        [7],                    7),
        ("one element – miss",       [7],                    2),
        ("no dups, middle",          [1, 2, 3, 4, 5],        3),
        ("no dups, first elem",      [1, 2, 3, 4, 5],        1),
        ("no dups, last elem",       [1, 2, 3, 4, 5],        5),
        ("no dups, absent",          [1, 2, 3, 4, 5],        6),
        ("dups in middle",           [1, 2, 2, 2, 3, 4],     2),
        ("dups at start",            [4, 4, 4, 5, 6],        4),
        ("dups at end",              [1, 2, 3, 9, 9, 9],     9),
        ("all duplicates",           [8, 8, 8, 8],           8),
        ("neg & pos mix",            [-5, -2, -2, 0, 0, 3],  0),
        ("target < min",             [2, 3, 4],              1),
        ("target > max",             [2, 3, 4],              5),
        ("large list",               list(range(100000))+[100000]*5, 100000),
    ]

    # ---------- a few random cases ----------
    for i in range(5):
        size   = random.randint(0, 1000)
        nums   = sorted(random.randint(-1000, 1000) for _ in range(size))
        target = random.choice(nums + [2000])  # 50 % chance “absent”
        cases.append((f"random {i+1}", nums, target))

    # ---------- executor ----------
    for desc, nums, target in cases:
        observed = last_position(nums, target)
        expected = (len(nums) - 1 - nums[::-1].index(target)) if target in nums else -1
        if observed == expected:
            print(f"PASS: {desc}")
        else:
            print(f"FAIL: {desc}  → expected {expected}, got {observed}")

# kick it off
if __name__ == "__main__":
    run_tests()
