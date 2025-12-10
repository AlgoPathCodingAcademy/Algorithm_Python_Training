nums = [1,2,5]
target = 12

dp = [0] * (target + 1)
solution = [-1] * (target + 1)

dp[0] = 1

for num in nums:
    for i in range(1,target+1):
        if i >= num:
            dp[i] += dp[i - num]
            
            if dp[i - num] != 0:
                solution[i] = i - num
        
print(dp)

print(solution)

result = []
current = target

while True:
    prev = solution[current]

    if prev == -1:
        break
    
    item_picked = current - prev

    print("item picked",item_picked)

    result.append(item_picked)
    
    current = prev
    
print(result)
