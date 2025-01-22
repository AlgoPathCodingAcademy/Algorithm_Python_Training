from collections import deque
N = 6
rows = N
cols = N
maze = []
for row in range(rows):
    row_ = []
    for col in range(cols):
        row_.append(0)
    maze.append(row_)
    
#print(maze)
start = (1,3)
end = (5,0)

visited = {}
visited[start] = True

to_do_list = deque()
to_do_list.append(start)

directions = [(-2,-1),(-2,1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2)]

# Add distance calculation
distance = {}
distance[(start)] = 0

# Debug Purpose
path = {}

isFound = False

while True:
    if len(to_do_list) == 0:
        break

    row,column = to_do_list.popleft()

    if (row,column) == end:
        isFound = True
        break
    
    for dx,dy in directions:
        new_row = dx + row
        new_column = dy + column
        
        if (new_row >= 0 and new_row < len(maze)) and \
            (new_column >= 0 and new_column < len(maze[0])) and \
            (maze[new_row][new_column] == 0):
                if (new_row,new_column) not in visited:
                    to_do_list.append((new_row,new_column))
                    visited[(new_row,new_column)] = True
                    # Debug Purpose
                    path[(new_row,new_column)] = row,column
                    # Add distance calculation
                    distance[(new_row,new_column)] = distance[(row,column)] + 1

if isFound:
    print("shortest path to dest", end, distance[end])
    # Debug print the full path from the beginning to the end
    print("Path Hash Table:",path)
    display_path = [(end)]
    while True:
        pre_path = path[end]
        end = pre_path
        display_path.append(end)
        if end == start:
            break
    print("Show one possible shortest path:", display_path[::-1])
else:
    print(-1)
