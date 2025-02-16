predecessors = {
    (2, 2): [(1, 2), (2, 1)],
    (1, 2): [(0, 2)],
    (2, 1): [(2, 0)],
    (0, 2): [(0, 1)],
    (2, 0): [(0, 0)],
    (0, 1): [(0, 0)]
}

paths = []
start = (0,0)

def helper(node, path):
    # TODO
      
end = (2,2)
helper(end, [end])
print("Reversed order (destination -> start):", paths)

# If you want the paths in the order from start to destination:
final_paths = [p[::-1] for p in paths]
print("Correct order (start -> destination):", final_paths)
