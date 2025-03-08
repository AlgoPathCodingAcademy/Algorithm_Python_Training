def minimumObstacles(grid):
    import heapq

    start = (0,0)
    
    rows = len(grid)
    columns = len(grid[0])

    end = (rows-1, columns-1)

    heap_list = []

    directions = [(0,-1),(0,1),(-1,0),(1,0)]

    distance = {}

    for i in range(rows):
        for j in range(columns):
            distance[(i,j)] = float("inf")
    distance[(0,0)] = 0

    heap_list = []
    heap_list.append((0,start))

    heapq.heapify(heap_list)

    # Note visited hashtable can no longer be used
    #visited = {}
    #visited[start] = True

    while True:
        if len(heap_list) == 0:
            return -1

        current_distance,(row,column) = heapq.heappop(heap_list)

        if (row,column) == end:
            return distance[end]

        for drow, dcolumn in directions:
            new_row = row + drow
            new_column = column + dcolumn
            if (new_row >= 0 and new_row < rows) and \
                (new_column >= 0 and new_column < columns):
                weight = grid[new_row][new_column]
                distance_neighbor = distance[(new_row,new_column)]
                updated_distance = distance[(row,column)] + weight

                current_distance = distance[(new_row,new_column)]
                if updated_distance < current_distance:
                    heapq.heappush(heap_list,(updated_distance,(new_row,new_column)))
                    distance[(new_row,new_column)] = updated_distance


print(minimumObstacles([[0,1,1],[1,1,0],[1,1,0]]))
print(minimumObstacles([[0,1,0,0,0],[0,1,0,1,0],[0,0,0,1,0]]))
