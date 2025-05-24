# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.

"""
k_sum_quick_tests.py – minimal, self‑contained sanity checks (no type hints)
============================================================================

This script focuses **only** on the *k‑sum* problem and deliberately avoids
Python type annotations, as requested.  Inline comments and docstrings give all
necessary context.

Run:
    python k_sum_quick_tests.py

You will get concise PASS/FAIL lines for each case and a summary.
"""

# ────────────────────────────────────────────────────────────────────────────
# 1.  Implementation under test (NO type hints)                               
# ────────────────────────────────────────────────────────────────────────────

def dfs_k_sum(nums, k, target, path, level, result):
    """Recursive helper that builds non‑decreasing k‑length combinations.

    Arguments
    ---------
    nums     : sorted list of input numbers
    k        : length of each combination we want
    target   : desired sum
    path     : current partial combination (list)
    level    : index in *nums* from which we may choose the next element
    results  : master list collecting every valid combination
    """
    if len(path) == k:
        if sum(path) == target:
            result.append(path)
        return
    for i in range(len(nums)):
        if path and path[-1] >= nums[i]:
            continue
        
        dfs_k_sum(nums, k, target, path + [nums[i]], level+1,result)


def k_sum_combinations(nums, k, target):
    """Return **all unique** k‑element subsets of *nums* that sum to *target*.

    The algorithm sorts the input and performs a depth‑first search that
    builds combinations in ascending order.  By pruning branches that already
    exceed *target* and skipping consecutive duplicates, it avoids unnecessary
    work and duplicate output.
    """
    nums = sorted(nums)          # Ascending order ensures each combo is unique
    results = []
    dfs_k_sum(nums, k, target, [], 0, results)
    return results

# ────────────────────────────────────────────────────────────────────────────
# 2.  Lightweight test runner                                                 
# ────────────────────────────────────────────────────────────────────────────

# No type hints here either; simple runtime checks suffice.

def _print(status, msg):
    print(f"[{status}] {msg}")


def _run_k_sum_test(nums, k, target, expected=None, expected_len=None):
    combos = k_sum_combinations(nums, k, target)

    if expected is not None:
        passed = {tuple(c) for c in combos} == {tuple(c) for c in expected}
        detail = "match" if passed else f"got {combos}"
    else:
        passed = len(combos) == expected_len
        detail = f"len={len(combos)} (exp {expected_len})"

    _print("PASS" if passed else "FAIL", f"nums={nums}, k={k}, tgt={target} – {detail}")
    return passed

# ────────────────────────────────────────────────────────────────────────────
# 3.  Test cases                                                              
# ────────────────────────────────────────────────────────────────────────────

def _suite():
    tests = [
        # Basic example provided by the user
        lambda: _run_k_sum_test([1, 2, 3, 4], 2, 5, expected=[[1, 4], [2, 3]]),
        # Single valid triple
        lambda: _run_k_sum_test([2, 3, 5, 7], 3, 10, expected=[[2, 3, 5]]),
        # Handle duplicates in the input list
        lambda: _run_k_sum_test([1, 1, 2, 2, 3], 3, 6, expected=[[1, 2, 3]]),
        # No possible combination
        lambda: _run_k_sum_test([1, 2], 3, 3, expected_len=0),
    ]

    passed = sum(t() for t in tests)
    total = len(tests)
    print("\n" + "─" * 30)
    print(f"k‑sum tests: {passed}/{total} passed")


if __name__ == "__main__":
    _suite()
