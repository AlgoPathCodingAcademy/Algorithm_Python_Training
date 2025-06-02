# ─────────────────────────────────────────────────────────────────────────────
# User-supplied function (find peak index in a mountain array)
# ─────────────────────────────────────────────────────────────────────────────
def binary_search(nums):
    start = 0
    end = len(nums) - 1

    while True:
        if start + 1 >= end:
            break

        middle = (start + end) // 2

        if nums[middle + 1] > nums[middle]:
            start = middle
        else:
            end = middle

    return start if nums[start] > nums[end] else end


# ─────────────────────────────────────────────────────────────────────────────
# Test-cases   (description, array)
# ─────────────────────────────────────────────────────────────────────────────
tests = [
    ("Example 1 – minimal mountain",              [0, 1, 0]),
    ("Example 2 – four elements",                 [0, 2, 1, 0]),
    ("Example 3 – given in prompt",               [0, 10, 5, 2]),
    ("Peak near centre, odd length",              [0, 5, 10, 7, 2]),
    ("Longer array with clear peak",              [3, 4, 5, 6, 8, 12, 9, 7, 4, 1]),
    ("Symmetric mountain (size 9)",               [1, 2, 3, 4, 5, 4, 3, 2, 1]),
    ("Negative values mountain",                  [-10, -5, -1, -3, -7]),
    ("Large 100-element mountain",                list(range(1, 51)) + list(range(49, 0, -1))),
]

print(f"{'Test':40}  {'Expected':>8}  {'Got':>8}  Result")
print("-" * 70)
all_pass = True
for desc, arr in tests:
    expected = arr.index(max(arr))            # ground-truth peak index
    got = binary_search(arr)
    ok = expected == got
    all_pass &= ok
    print(f"{desc:40}  {expected:8}  {got:8}  {'PASS' if ok else 'FAIL'}")

if all_pass:
    print("\n✅  All tests passed!")
