lst = [1,2,3,4]
k = 2
target = 5
result = []

def dfs_k_sum(path, level):
    if len(path) == k:
        if sum(path) == target:
            result.append(path)
        return
    for i in range(len(lst)):
        if path and path[-1] >= lst[i]:
            continue
        
        dfs_k_sum(path + [lst[i]], level+1)

dfs_k_sum([],-1)
print(result)
