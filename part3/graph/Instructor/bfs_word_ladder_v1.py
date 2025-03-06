def getNeighbors(current, dict_):
    result = []

    for item in dict_:
        diff_counter = 0
        for i in range(len(current)):
            if current[i] != item[i]:
                diff_counter += 1

        if diff_counter == 1:
            result.append(item)

    return result

def isOneWordDiff(old, new):
    diff_counter = 0
    for i in range(len(old)):
        if old[i] != new[i]:
            diff_counter += 1

    if diff_counter == 1:
        return True
    else:
        return False


def ladder_length(start, end, dict):
    # write your code here
    from collections import deque
    visited = {}
    visited[start] = True

    to_do_list = deque()
    to_do_list.append(start)

    path = {}
    path[start] = 1

    isPossible = False

    current = None

    while True:
        if len(to_do_list) == 0:
            break

        current = to_do_list.popleft()

        if isOneWordDiff(current,end):
            isPossible = True
            break

        neighbors = getNeighbors(current, dict)

        for neighbor in neighbors:
            if neighbor not in visited:
                visited[neighbor] = True
                to_do_list.append(neighbor)
                path[neighbor] = path[current] + 1

    if isPossible:
        return path[current] + 1
    else:
        return 0


start ="hit"
end = "cog"
dict =["hot","dot","dog","lot","log"]

print(ladder_length(start,end,dict))
