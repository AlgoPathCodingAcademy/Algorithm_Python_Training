graph = {
    1: [(2, 0), (4, 1)],
    2: [(1, 0), (3, 1)],
    3: [(2, 1), (5, 0)],
    4: [(1, 1), (5, 1)],
    5: [(3, 0), (4, 1)]
}

from collections import deque

start = 1
to_do_list = deque()

to_do_list.append(start)

path = {}

for node in graph:
    path[node] = float("inf")
    
path[start] = 0

while True:
    if len(to_do_list) == 0:
        break

    current = to_do_list.popleft()
    
    neighbors = graph[current]
    
    for neighbor, weight in neighbors:
        if path[current] + weight < path[neighbor]:
            path[neighbor] = path[current] + weight
            if weight == 0:
                to_do_list.appendleft(neighbor)
            else:
                to_do_list.append(neighbor)
                
print(path)
