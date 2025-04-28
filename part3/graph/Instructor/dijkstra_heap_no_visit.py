from collections import deque
import heapq
graph = {
    1: [(2, 0), (4, 1)],
    2: [(1, 0), (3, 1)],
    3: [(2, 1), (5, 0)],
    4: [(1, 1), (5, 1)],
    5: [(3, 0), (4, 1)]
}

startNode = 1
start = (0,startNode)
heap = []
heap.append(start)

weights = {}
for node in graph:
    weights[node] = float("inf")
    
weights[1] = 0

while True:
    if len(heap) == 0:
        break
    
    current_weight,current_node = heapq.heappop(heap)
   
    # If we've found a better path previously, skip this outdated entry
    if current_weight > weights[current_node]:
        continue


    for neighbor_node, neighbor_weight in graph[current_node]:
        weight = current_weight + neighbor_weight
        if weight < weights[neighbor_node]:
            weights[neighbor_node] = weight
            heapq.heappush(heap, (weight,neighbor_node))

print(weights)
