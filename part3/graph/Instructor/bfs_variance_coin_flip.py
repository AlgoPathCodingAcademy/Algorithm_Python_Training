# Flip Coins Problem

from collections import deque

def getNeighbors(node):
  #flip two adj items
  list_node = list(node)
  neighbors = []
  for i in range(len(list_node)-1):
    flip_list = list_node[:]
    if flip_list[i] == "H":
      flip_list[i] = "T"
    else:
      flip_list[i] = "H"

    if flip_list[i+1] == "H":
      flip_list[i+1] = "T"
    else:
      flip_list[i+1] = "H"

    neighbors.append("".join(flip_list))

  return neighbors
      
nums = int(input())
node = list(input())

target = ""
for i in range(nums):
  target = target + "H"

visited = {}
visited["".join(node)] = True

to_do_list = deque()
to_do_list.append("".join(node))

distance = {}
distance["".join(node)] = 0

while True:
  if len(to_do_list) == 0:
    break

  current_item = to_do_list.popleft()

  if current_item == target:
    break

  # check neighbors
  neighbors = getNeighbors(current_item)
  # check if visited
  for neighbor in neighbors:
    if neighbor not in visited:
      visited[neighbor] = True
      to_do_list.append(neighbor)
      distance[neighbor] = distance[current_item] + 1

print(distance[target])
