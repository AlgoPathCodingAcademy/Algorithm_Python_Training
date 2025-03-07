def getNeighbors(current, nums, level):
    neighbors = []

    neighbors.append(current)
    neighbors.append(tuple(list(current) + [nums[level]]))

    return neighbors

def subsets(nums):
    from collections import deque
    # write your code here
    level = -1 
    start = ((), level)

    to_do_list = deque()
    to_do_list.append(start)

    output = {}

    while True:
        if len(to_do_list) == 0:
            break

        current, level = to_do_list.popleft()
        # collect the last layer
        if level not in output:
            output[level] = [list(current)]
        else:
            output[level].append(list(current))

        if level == len(nums)-1:
            continue

        neighbors = getNeighbors(current, nums, level+1)

        # Note: Unlike normal BFS, we shouldn't use visited
        for neighbor in neighbors:
            to_do_list.append((neighbor, level+1))

    final = []
    for item in output[len(nums)-1]:
        final.append(sorted(item))

    return final
    
nums = [1,2,3]
result = subsets(nums)
print(result)
