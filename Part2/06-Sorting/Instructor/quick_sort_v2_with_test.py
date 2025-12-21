import random

def partition(nums, start, end):
    pivot = nums[end]
    left = start
    right = end - 1

    while True:
        if nums[left] < pivot:
            left += 1
        else:
            nums[left], nums[right] = nums[right], nums[left]
            right -= 1

        if left > right:
            break

    nums[left], nums[end] = nums[end], nums[left]
    return left


def quick_sort(nums, start, end):
    if start >= end:
        return

    p = partition(nums, start, end)
    quick_sort(nums, start, p - 1)
    quick_sort(nums, p + 1, end)

# Generate random test data
nums = [random.randint(-1000, 1000) for _ in range(1000)]

# Keep a correct reference result
expected = sorted(nums)

# Apply the student's sorting algorithm
quick_sort(nums, 0, len(nums) - 1)

# Compare results
if nums == expected:
    print("PASS: The sorting algorithm works correctly.")
else:
    print("FAIL: The sorting algorithm is incorrect.")
