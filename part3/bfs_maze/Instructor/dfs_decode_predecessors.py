# Predecessors dictionary for the new test case:
predecessors = {
    (2,2): [(1,2), (2,1)],
    (1,2): [(0,2), (1,1)],
    (2,1): [(2,0), (1,1)],
    (0,2): [(0,1)],
    (1,1): [(0,1), (1,0)],
    (2,0): [(1,0)],
    (0,1): [(0,0)],
    (1,0): [(0,0)]
}

paths = []

start = (0,0)

def helper(node,path):
    if node == start:
        paths.append(path)
        return
    
    #print("node",node,"path",path)
    for item in predecessors[node]:
        helper(item,path+[item])
      
end = (2,2)
helper(end,[end])

print(paths)
