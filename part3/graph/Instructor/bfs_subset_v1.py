def getNeighbors(current, nums):
    result = []
    for num in nums:
        if current and current[-1] >= num:
            continue

        subResult = list(current) + [num]
        result.append(tuple(subResult))

    return result

def subsets(nums):
    # write your code here
    from collections import deque
    start = ()
    queue = deque()
    queue.append(start)
    result = []

    visited = {}
    visited[start] = True

    while True:
        if len(queue) == 0:
            break

        current = queue.popleft()
        result.append(list(current))

        neighbors = getNeighbors(current,nums)
        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = True
                queue.append(neighbor)

    return result
    
lst_ = [1,2,3]
result = subsets(lst_)
print(result)
