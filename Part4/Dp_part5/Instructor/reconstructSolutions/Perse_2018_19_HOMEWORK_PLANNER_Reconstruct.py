nums = int(input())
capacity = int(input())
weights = [int(input()) for _ in range(nums)]

dp = [[0] * (capacity + 1) for _ in range(nums + 1)]
parent = [[(-1, -1)] * (capacity + 1) for _ in range(nums + 1)]

for i in range(1, nums + 1):
    w = weights[i-1]
    for t in range(capacity + 1):

        # skip item i-1
        dp[i][t] = dp[i-1][t]
        parent[i][t] = (i-1, t)

        # take item i-1
        if t >= w and dp[i-1][t-w] + w > dp[i][t]:
            dp[i][t] = dp[i-1][t-w] + w
            parent[i][t] = (i-1, t-w)

# list the optimum solution
current_nums_items = nums
current_capacity = capacity

items = []

while True:
    prev_nums_items, prev_capacity = parent[current_nums_items][current_capacity]
    
    if prev_nums_items == -1:
        break
    
    if current_capacity != prev_capacity:
        items.append(weights[current_nums_items-1])
    
    current_nums_items = prev_nums_items
    current_capacity = prev_capacity

print(items)
