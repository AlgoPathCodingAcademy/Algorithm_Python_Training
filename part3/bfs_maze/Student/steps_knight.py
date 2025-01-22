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

start = (1,3)
end = (5,0)

visited = {}
visited[start] = True

to_do_list = deque()
to_do_list.append(start)

# Add distance calculation
distance = {}
distance[(start)] = 0
