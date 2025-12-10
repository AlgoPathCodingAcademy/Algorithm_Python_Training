n = 10
dp = [1] * (n+1)
#solution = [1] * (n+1)
solution = [-1] * (n+1)

dp[1] = 1

for i in range(2, n+1):
    max_result = float("-inf")
    max_values = ()
    for j in range(1,i):
        if dp[i-j] * j > (i-j) * j:
            if dp[i-j] * j > max_result:
                max_result = dp[i-j] * j
                max_values = (True,j)
        else:
            if (i-j) * j > max_result:
                max_result = (i-j) * j
                max_values = (False,j)
            
    dp[i] = max_result
    solution[i] = max_values
    
            
print(dp)
print(solution)

current_value = n
answers = []

while True:
    prev_value = solution[current_value]
    if prev_value == -1:
        break
    
    prev_dp_status, prev_last_number = prev_value
    
    if prev_dp_status:
        answers.append(prev_last_number)
        current_value = current_value - prev_last_number
    else:
        current_value = current_value - prev_last_number
        answers.append(current_value)
        answers.append(prev_last_number)
        break

print(answers)
