def quickSelect(lst, start,end):
    pivot = lst[start]
    left = start
    start = start + 1

    while True:
        while True:

            if start > end:
                break

            if lst[start] > pivot:
                break

            start = start + 1

        while True:
            if start > end:
                break

            if lst[end] < pivot:
                break

            end = end - 1

        if start > end:
            break

        lst[start],lst[end] = lst[end],lst[start]

    lst[left],lst[end] = lst[end],lst[left]

    return end

def dfs(lst, start,end):
    if len(lst) == 0:
        return

    if start >= end:
        return
    
    index = quickSelect(lst,start,end)
    dfs(lst,start,index-1)
    dfs(lst,index+1,end)

def sort_integers2(a):
    # write your code here
    dfs(a,0,len(a)-1)
    return a
    

import random
from copy import deepcopy

# ------------------------------------------------------------------
# test harness
# ------------------------------------------------------------------
def run_quicksort_tests():
    # ---------- fixed, easy-to-inspect cases
    deterministic = [
        [],                                 # 0  empty
        [42],                               # 1  single element
        [2, 1],                             # 2  two, descending
        [1, 2],                             # 3  two, ascending
        [3, 5, 3, 3, 2, 5, 1],              # 4  many duplicates
        [7, 6, 5, 4, 3, 2, 1],              # 5  already descending
        [-3, 0, 2, -3, 7, -1],              # 6  negatives + duplicates
        [1, 1, 1, 1, 1],                    # 7  all equal
        list(range(10)),                    # 8  already ascending
        list(range(9, -1, -1)),             # 9  worst-case order for naïve pivot
    ]

    # ---------- random stress cases (same seed → reproducible)
    random.seed(2025)
    random_cases = [
        random.choices(range(-50, 51), k=n)           # values from –50…50
        for n in (20, 100, 1000)                      # different sizes
    ]

    test_cases = deterministic + random_cases

    # run them
    for idx, arr in enumerate(test_cases):
        original = deepcopy(arr)
        out      = sort_integers2(arr)            # in-place; returns same list
        assert out == sorted(original), \
            f"❌  test #{idx} failed: {original} ➜ {out}"

    print(f"✅  all {len(test_cases)} quick-sort tests passed!")

# ------------------------------------------------------------------
# uncomment to execute the tests when this file is run directly
# ------------------------------------------------------------------
if __name__ == "__main__":
    run_quicksort_tests()
