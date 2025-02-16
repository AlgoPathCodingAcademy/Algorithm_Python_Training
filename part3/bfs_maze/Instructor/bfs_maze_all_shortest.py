from collections import deque

#maze = [
#    [0,1,0,0],
#    [0,0,0,1],
#    [1,0,0,0],
#    [0,1,0,0]]

maze = [
    [0,0,0],
    [0,0,0],
    [1,0,0]]
    
start = (0,0)
end = (2,2)

visited = {}
visited[start] = True

to_do_list = deque()
to_do_list.append(start)

full_path = {}
full_path[start] = []  # start has no parent

directions = [(-1,0),(1,0),(0,-1),(0,1)]

# Add distance calculation
distance = {}
distance[(start)] = 0

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
    
    for dx,dy in directions:
        new_row = dx + row
        new_column = dy + column
        
        if (new_row >= 0 and new_row < len(maze)) and \
            (new_column >= 0 and new_column < len(maze[0])) and \
            (maze[new_row][new_column] == 0):
                
            new_distance = distance[(row,column)] + 1
            if (new_row,new_column) not in distance:
                to_do_list.append((new_row,new_column))
                full_path[(new_row,new_column)] = [(row,column)]
                distance[(new_row,new_column)] = new_distance
            elif new_distance == distance[(new_row,new_column)]:
                full_path[(new_row,new_column)].append((row,column))
                

print("full_path", full_path)

paths = []

start = (0,0)

def helper(node,path):
    if node == start:
        paths.append(path)
        return

    #print("node",node,"path",path)
    for item in full_path[node]:
        helper(item,path+[item])
      
end = (2,2)
helper(end,[(end)])

for path in paths:
    print(path[::-1])
