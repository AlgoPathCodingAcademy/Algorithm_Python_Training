from collections import deque

maze = [
    [0,1,0,0],
    [0,0,0,1],
    [1,0,0,0],
    [0,1,0,0]]
    
start = (0,0)
end = (3,3)

visited = {}
visited[start] = True

to_do_list = deque()
to_do_list.append(start)

directions = [(-1,0),(1,0),(0,-1),(0,1)]

# Debug Purpose
path = {}
path[start] = None

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

# Debug print the full path from the beginning to the end
print("Debug:Path Hash Table:",path)
display_path = []
while True:
    display_path.append(end)
    pre_path = path[end]
    end = pre_path
    if end == None:
        break
print("Debug:Show one possible shortest path:", display_path[::-1])

print(isFound)
