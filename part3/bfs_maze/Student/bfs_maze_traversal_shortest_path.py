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

# Add distance calculation
distance = {}
distance[(start)] = 0
