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
    
    # If the value at `start` is already the target, there is **no strictly
    # smaller element** in the array.  The problem statement says we should
    # return -1 when “no number smaller than target” exists.
    if nums[start] == target:
        return -1
    
    # At this point `end` is the first index whose value is ≥ target.
    # If *that* value still isn’t the target, it means the target does **not**
    # appear anywhere in the array.  Per the spec, we return -1 when the
    # target is absent.
    if nums[end] != target:
        return -1

    return start
# ――――――――――――――――――――――――――――――――――――――――――――――――――――――

array = [10, 20, 20, 35, 50, 50, 65, 80, 95, 110]

# (label, target, expected_result)
tests = [
    ("duplicate target present",              50, 3),   # largest index < 50  → 3
    ("unique target present",                 65, 5),   # largest index < 65  → 5
    ("target absent – in-between value",      30, -1),  # 30 not in list      → -1
    ("target absent – greater than all",     100, -1),  # 100 not in list     → -1
    ("no smaller number than target",         10, -1),  # nothing < 10        → -1
]

for label, tgt, expected in tests:
    got = binary_search(array, tgt)
    print(f"{label:35} target={tgt:<4}  expected={expected:<3}  got={got:<3}  →",
          "PASS" if got == expected else "FAIL")
