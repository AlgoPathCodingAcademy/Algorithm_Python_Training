def quick_select(lst, start,end):
    pivot_index = start
    left = start + 1
    right = end

    while True:
        while True:
            if left > right:
                break

            if lst[left] > lst[pivot_index]:
                break

            left = left + 1

        while True:
            if left > right:
                break

            if lst[right] < lst[pivot_index]:
                break

            right = right - 1

        if left > right:
            break

        # swap
        lst[left],lst[right] = lst[right],lst[left]

    # final swap right with the pivot
    lst[pivot_index],lst[right] = lst[right],lst[pivot_index]

    return right

def dfs_find(lst,start,end, matchedIndex):
    middle_index = quick_select(lst,start,end)
    if middle_index > matchedIndex:
        return dfs_find(lst,start,middle_index-1,matchedIndex)
    elif middle_index < matchedIndex:
        return dfs_find(lst,middle_index+1,end,matchedIndex)
    else:
        return lst[middle_index]

def kth_largest_element(k, nums):
    # write your code here
    output = dfs_find(nums,0,len(nums)-1,len(nums)-k)
    return output
    
    
import random

# ------------- your functions (quick_select, dfs_find, kth_largest_element) go here -------------

def run_tests():
    deterministic = [
        (1, [1, 3, 4, 2], 4),                # example 1
        (3, [9, 3, 2, 4, 8], 4),             # example 2
        (2, [5, 5, 5, 5], 5),                # all duplicates
        (2, [5, 4, 3, 2, 1], 4),             # descending order
        (2, [-1, -5, 10, 7], 7),             # negatives + positives
        (3, [2, 3, 1], 1),                   # k == len(nums)
    ]

    random.seed(2025)                        # reproduce the same lists each run
    for n in (10, 20, 50):
        arr = random.sample(range(-100, 101), n)
        k   = random.randint(1, n)
        deterministic.append((k, arr, sorted(arr, reverse=True)[k-1]))

    ok = True
    for idx, (k, nums, expect) in enumerate(deterministic):
        result = kth_largest_element(k, nums.copy())  # copy: algorithm is in-place
        if result == expect:
            print(f"✅  Test {idx}: PASS")
        else:
            print(f"❌  Test {idx}: FAIL — k={k}, nums={nums}, "
                  f"expected {expect}, got {result}")
            ok = False

    print(f"\nAll {len(deterministic)} tests {'passed' if ok else 'had failures'}.")

if __name__ == "__main__":
    run_tests()
