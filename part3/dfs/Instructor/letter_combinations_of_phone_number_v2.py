"""
phone_digit_combination_test.py
===============================

A **single self‑contained script** that includes

* an implementation of `letter_combinations` (DFS)
* a handful of sanity tests you can run immediately.

Usage
-----
```
python phone_digit_combination_test.py
```
You’ll get a concise PASS/FAIL report for each case.
"""

# ────────────────────────────────────────────────────────────────────────────
# Implementation
# ────────────────────────────────────────────────────────────────────────────
hashTable = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"}

def dfs_work(numbers,path,level,result):
    if level == len(numbers):
        result.append(path)
        return
    letters = hashTable[numbers[level]]
    for letter in letters:
        dfs_work(numbers, path+letter,level + 1,result)

def letter_combinations(digits):
    result = []
    dfs_work(digits,"",0,result)
    return result

# ────────────────────────────────────────────────────────────────────────────
# Lightweight tests
# ────────────────────────────────────────────────────────────────────────────

from typing import Any, Sequence

def _run_test(
    digits: str,
    *,
    expected: Sequence[str] | None = None,
    expected_len: int | None = None,
    expect_error: bool = False,
) -> bool:
    """Execute one test case and print the outcome."""
    try:
        combos = letter_combinations(digits)
        if expect_error:
            print(f"[FAIL] input={digits!r} – expected error but got result")
            return False

        if expected is not None:
            passed = sorted(combos) == sorted(expected)
            detail = "matches expected list" if passed else f"got {combos}"
        elif expected_len is not None:
            passed = len(combos) == expected_len
            detail = f"length {len(combos)} (expected {expected_len})"
        else:
            raise ValueError("Test case must supply expected or expected_len")

        status = "PASS" if passed else "FAIL"
        print(f"[{status}] input={digits!r} – {detail}")
        return passed

    except Exception as exc:
        if expect_error:
            print(f"[PASS] input={digits!r} – raised {exc.__class__.__name__} as expected")
            return True
        else:
            print(f"[FAIL] input={digits!r} – unexpected {exc.__class__.__name__}: {exc}")
            return False


def _main() -> None:
    tests = [
        {"digits": "2", "expected": ["a", "b", "c"]},
        {
            "digits": "23",
            "expected": [
                "ad",
                "ae",
                "af",
                "bd",
                "be",
                "bf",
                "cd",
                "ce",
                "cf",
            ],
        },
        {"digits": "7", "expected": list("pqrs")},
        {"digits": "79", "expected_len": 16},  # 4 × 4
        {"digits": "234", "expected_len": 27},  # 3 × 3 × 3
    ]

    passed = sum(
        _run_test(
            t["digits"],
            expected=t.get("expected"),
            expected_len=t.get("expected_len"),
            expect_error=t.get("expect_error", False),
        )
        for t in tests
    )
    total = len(tests)
    print(f"Summary: {passed}/{total} tests passed.")


if __name__ == "__main__":
    _main()

