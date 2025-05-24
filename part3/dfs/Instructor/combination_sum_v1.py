lst = [2,3,6,7]

target = 7

result = []
def dfs_combination_sum(path):
    total = sum(path)
    if total >= target:
        if total == target:
            result.append(path)
        return
    for i in range(len(lst)):
        if path and path[-1] > lst[i]:
            continue
        dfs_combination_sum(path+[lst[i]])
        

dfs_combination_sum([])

print(result)
