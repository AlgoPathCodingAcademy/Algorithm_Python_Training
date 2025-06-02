# ─────────────────────────────────────────────────────────────────────────────
# Function under test – find minimum element in a rotated sorted array
# (your exact code, unchanged)
# ─────────────────────────────────────────────────────────────────────────────
def binary_search(nums):
    start = 0
    end   = len(nums) - 1

    while True:
        if start + 1 >= end:
            break

        middle = (start + end) // 2

        # Compare to last element → tells us which half is sorted
        if nums[middle] > nums[len(nums) - 1]:
            start = middle            # pivot is to the right
        else:
            end = middle              # pivot is at mid or to the left

    return nums[end] if nums[start] > nums[end] else nums[start]


# ─────────────────────────────────────────────────────────────────────────────
# Test-cases   (label, array, expected_min)
# ─────────────────────────────────────────────────────────────────────────────
tests = [
    # — typical rotations —
    ("no rotation (already sorted)",           [0, 1, 2, 4, 5, 6, 7],               0),
    ("pivot in middle",                        [4, 5, 6, 7, 0, 1, 2],               0),
    ("pivot near end",                         [1, 2, 4, 5, 6, 7, 0],               0),
    ("pivot near beginning",                   [6, 7, 0, 1, 2, 4, 5],               0),
    ("single left rotation",                   [7, 0, 1, 2, 4, 5, 6],               0),
    ("single right rotation",                  [2, 4, 5, 6, 7, 0, 1],               0),

    # — small arrays —
    ("two elements – rotated",                 [2, 1],                              1),
    ("two elements – not rotated",             [1, 2],                              1),
    ("single element",                         [4],                                 4),

    # — larger array —
    ("large 1000-element, pivot at last",      list(range(1, 1000)) + [0],          0),
]

# ─────────────────────────────────────────────────────────────────────────────
# Run the suite
# ─────────────────────────────────────────────────────────────────────────────
print(f"{'Test':35}  {'Expected':>8}  {'Got':>8}  Result")
print("-" * 65)
all_ok = True
for label, arr, expect in tests:
    got = binary_search(arr)
    ok  = got == expect
    all_ok &= ok
    print(f"{label:35}  {expect:8}  {got:8}  {'PASS' if ok else 'FAIL'}")

if all_ok:
    print("\n✅  All tests passed!")
else:
    print("\n❌  Some tests failed.")
