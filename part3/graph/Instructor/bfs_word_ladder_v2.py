def getNeighbors(current, dict_):
    result = []
    # Build pattern
    for i in range(len(current)):
        word = current[0:i]+ "*" + current[i+1:]
        if word in dict_:
            result += dict_[word]

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

    dic_pattern_map = {}

    for item in dict:
        for index in range(len(item)):
            word_pattern = item[0:index] + "*" + item[index+1:]
            if word_pattern not in dic_pattern_map:
                dic_pattern_map[word_pattern] = []
                dic_pattern_map[word_pattern].append(item)
            else:
                dic_pattern_map[word_pattern].append(item)


    while True:
        if len(to_do_list) == 0:
            break

        current = to_do_list.popleft()

        if isOneWordDiff(current,end):
            isPossible = True
            break

        neighbors = getNeighbors(current, dic_pattern_map)

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
