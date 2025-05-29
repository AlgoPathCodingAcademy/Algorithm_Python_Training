def binary_search_first(nums, target):
    if not nums:
        return -1                    # empty list → not found

    left, right = 0, len(nums) - 1

    while True:
        # ── stop when ≤ 2 elements remain ─────────────────────────
        if left + 1 >= right:        #  ← was the loop-guard before
            break

        # ── normal binary-search step ─────────────────────────────
        mid = (left + right) // 2
        if nums[mid] < target:
            left = mid               # discard left half (inc. mid)
        else:                        # nums[mid] ≥ target
            right = mid              # keep mid; might be the first

    # ── post-processing: check the surviving 1–2 elements ────────
    if nums[left] == target:
        return left
    if nums[right] == target:        # runs only when left != right
        return right
    return -1                        # target absent

import random

def _is_valid(nums, target, result):
    """
    Returns True when `result` is a legal answer for (nums, target):
      • -1 is legal only if target is absent
      • Any in-range index is legal if it points to target
    """
    if result == -1:
        return target not in nums
    return 0 <= result < len(nums) and nums[result] == target


def run_tests():
    # —— deterministic cases ——
    tests = [
        ([], 42),                        # empty list
        ([5], 5), ([5], -5),             # single element: hit & miss
        ([1, 2, 3, 4, 5], 3),            # target in middle
        ([1, 2, 3, 4, 5], 1),            # target at left edge
        ([1, 2, 3, 4, 5], 5),            # target at right edge
        ([1, 2, 3, 4, 5], 6),            # target absent
        ([1, 1, 2, 2, 2, 3], 2),         # duplicates – any match OK
        ([1, 1, 1, 1], 1),               # all duplicates (hit)
        ([1, 1, 1, 1], 0),               # all duplicates (miss)
        ([-10, -3, 0, 2, 5], -10),       # negatives, target at start
        ([-10, -3, 0, 2, 5], 5),         # negatives & positives, target at end
        (list(range(1_000_000)), 999_999) # big input, target near end
    ]

    # —— a few randomized cases for extra confidence ——
    for _ in range(5):
        size   = random.randint(1, 1000)
        nums   = sorted(random.sample(range(-2000, 2000), size))
        target = random.choice(nums + [3000])      # 50 % chance of a “miss”
        tests.append((nums, target))

    # —— execute and report ——
    for idx, (nums, target) in enumerate(tests, 1):
        result = binary_search_first(nums, target)
        if not _is_valid(nums, target, result):
            short = f"{nums[:10]}…" if len(nums) > 10 else nums
            print(f"FAIL on case #{idx}: nums={short}  target={target}  got={result}")
            return
    print("PASS")


if __name__ == "__main__":
    run_tests()
