"""
combination_sum_quick_tests.py – minimal, self‑contained checks (no type hints)
==============================================================================

This script contains **only** the Combination‑Sum implementation and a handful
of sanity tests.  All type annotations are omitted per the earlier request.

Run:
    python combination_sum_quick_tests.py

It prints concise PASS/FAIL lines for each case and a final summary.
"""

# ────────────────────────────────────────────────────────────────────────────
# 1.  Implementation under test (NO type hints)                               
# ────────────────────────────────────────────────────────────────────────────

def dfs_combination_sum(nums, target, path, result):
    total = sum(path)
    if total >= target:
        if total == target:
            result.append(path)
        return
    for i in range(len(nums)):
        if path and path[-1] > nums[i]:
            continue
        dfs_combination_sum(nums, target, path+[nums[i]], result)


def combination_sum(nums, target):
    """Return all unique combinations of *nums* that sum to *target*.

    Each number may be used multiple times.  Combinations are returned in
    non‑decreasing order (e.g., [2,2,3] not [3,2,2]).
    """
    nums = sorted(nums)
    results = []
    dfs_combination_sum(nums, target, [], results)
    return results

# ────────────────────────────────────────────────────────────────────────────
# 2.  Lightweight test runner                                                 
# ────────────────────────────────────────────────────────────────────────────

def _print(status, msg):
    print(f"[{status}] {msg}")


def _run_comb_sum_test(nums, target, expected):
    combos = combination_sum(nums, target)
    passed = {tuple(c) for c in combos} == {tuple(c) for c in expected}
    detail = "match" if passed else f"got {combos}"
    _print("PASS" if passed else "FAIL", f"nums={nums}, tgt={target} – {detail}")
    return passed

# ────────────────────────────────────────────────────────────────────────────
# 3.  Test cases                                                              
# ────────────────────────────────────────────────────────────────────────────

def _suite():
    tests = [
        # Example provided by the user
        lambda: _run_comb_sum_test([2, 3, 6, 7], 7, expected=[[2, 2, 3], [7]]),
        # Multiple solutions with repeats
        lambda: _run_comb_sum_test([2, 3, 5], 8, expected=[[2, 2, 2, 2], [2, 3, 3], [3, 5]]),
        # No possible combination
        lambda: _run_comb_sum_test([3, 5], 2, expected=[]),
        # Empty input list
        lambda: _run_comb_sum_test([], 5, expected=[]),
        # Target zero should yield one valid combination: the empty list
        lambda: _run_comb_sum_test([1, 2], 0, expected=[[]]),
    ]

    passed = sum(t() for t in tests)
    total = len(tests)
    print("\n" + "─" * 30)
    print(f"combination‑sum tests: {passed}/{total} passed")


if __name__ == "__main__":
    _suite()

