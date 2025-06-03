# ──────────────────────────────────────────────────────────────
#  Binary-search helpers (no class wrapper)
# ──────────────────────────────────────────────────────────────
def binary_search_row(matrix, target):
    start, end = 0, len(matrix) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if matrix[mid][0] > target:
            end = mid
        else:
            start = mid
    return start, end

def binary_search_column(matrix, row_idx, target):
    start, end = 0, len(matrix[0]) - 1
    while start + 1 < end:
        mid = (start + end) // 2
        if matrix[row_idx][mid] > target:
            end = mid
        else:
            start = mid
    return matrix[row_idx][start] == target or matrix[row_idx][end] == target

def search_matrix(matrix, target):
    start, end = binary_search_row(matrix, target)
    if binary_search_column(matrix, start, target):
        return True
    if binary_search_column(matrix, end, target):
        return True
    return False


# ──────────────────────────────────────────────────────────────
#  Test-cases  (label, matrix, target, expected)
# ──────────────────────────────────────────────────────────────
tests = [
    ("target present - mid row", [[1,3,5],[7,9,11],[13,15,17]], 9,  True),
    ("target absent",            [[1,3,5],[7,9,11],[13,15,17]], 4,  False),
    ("first element",            [[1,3,5],[7,9,11],[13,15,17]], 1,  True),
    ("last element",             [[1,3,5],[7,9,11],[13,15,17]],17,  True),
    ("single row",               [[2,4,6,8,10,12]],              8,  True),
    ("single column",            [[1],[3],[5],[7]],              7,  True),
    ("single number - found",    [[42]],                         42, True),
    ("single number - absent",   [[42]],                         7,  False),
]

# ──────────────────────────────────────────────────────────────
#  Run suite
# ──────────────────────────────────────────────────────────────
print(f"{'Test':30}  {'Expected':>8}  {'Got':>8}  Result")
print("-"*60)
all_pass = True
for label, mat, tgt, expected in tests:
    got = search_matrix(mat, tgt)
    ok  = got == expected
    all_pass &= ok
    print(f"{label:30}  {str(expected):>8}  {str(got):>8}  {'PASS' if ok else 'FAIL'}")

print("\n✅ All tests passed!" if all_pass else "\n❌ Some tests failed.")
