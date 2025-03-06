from collections import deque

def getNeighbors(current, level, nums):
    result = []

    if level == len(nums):
        return None

    list_on_ = list(current) + [nums[level]]
    list_off_ = list(current)
    result.append(tuple(list_off_))
    result.append(tuple(list_on_))

    return result

def subsets(nums):
    # write your code here
    start = ()
    queue = deque()
    queue.append((start,0))
    result = {}

    visited = {}
    visited[start] = True

    while True:
        if len(queue) == 0:
            break

        current, level = queue.popleft()

        if level not in result:
            result[level] = [[]]
        else:
            result[level].append(list(current))

        neighbors = getNeighbors(current, level, nums)

        if neighbors != None:
            for neighbor in neighbors:
                queue.append((neighbor,level+1))

    output = []
    for level in result:
        output.append(result[level])
    
    final_answer = []
    outputs = sorted(output[-1])
    for answer in outputs:
        final_answer.append(sorted(answer))

    return final_answer
    
lst_ = [1,2,3]
result = subsets(lst_)
print(result)
