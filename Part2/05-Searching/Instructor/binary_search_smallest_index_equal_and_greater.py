# ―― function exactly as given ―――――――――――――――――――――――――――――――――
def binary_search(nums, target):
    start = 0
    end = len(nums) - 1

    while True:
        if start + 1 >= end:
            break

        middle = (start + end) // 2

        if nums[middle] < target:
            start = middle
        else:
            end = middle
    
    # ── Case 1: BOTH surviving values are ≥ target ────────────────────────────
    if nums[end] >= target and nums[start] >= target:
    #  • nums[start] is the lower index (closer to the left side of the list).
    #  • Because both nums[start] and nums[end] meet the ≥ target condition,
    #    nums[start] must be **the first (smallest) index whose value ≥ target**.
    #  • Return start immediately.
        return start

    # ── Case 2: ONLY the value at `end` is ≥ target ───────────────────────────
    if nums[end] >= target:
    #  • This happens when nums[start] < target < nums[end]
    #    (or equal to nums[end] if target is present once).
    #  • Hence nums[end] is the first index where value ≥ target.
        return end
    
    return -1

# ────────────────────────────────────────────────────────────────────────────────
# Test-cases   (description, nums, target, expected)
# ────────────────────────────────────────────────────────────────────────────────
tests = [
    ("duplicate target present",               [10,20,20,35,50,50,65,80,95,110], 50, 4),
    ("unique target present",                  [10,20,20,35,50,50,65,80,95,110], 65, 6),
    ("target absent – pick next larger",       [10,20,20,35,50,50,65,80,95,110], 30, 3),
    ("target smaller than every element",      [10,20,20,35,50,50,65,80,95,110], 5,  0),
    ("target larger than every element",       [10,20,20,35,50,50,65,80,95,110], 130, -1),
    ("single element – found",                 [7],                                7,  0),
    ("single element – smaller than element",  [7],                                6,  0),
    ("single element – greater than element",  [7],                                8,  -1),
    ("two elements – target between",          [5, 10],                            6,  1),
    ("two elements – target smaller than all", [5, 10],                            2,  0),
]

# ────────────────────────────────────────────────────────────────────────────────
# Run tests
# ────────────────────────────────────────────────────────────────────────────────
for desc, nums, tgt, expected in tests:
    got = binary_search(nums, tgt)
    status = "PASS" if got == expected else "FAIL"
    print(f"{desc:35}  target={tgt:<3}  expected={expected:<3}  got={got:<3} → {status}")

    # Uncomment the next line if you prefer hard assertions
    # assert got == expected, f"{desc}: expected {expected}, got {got}"
