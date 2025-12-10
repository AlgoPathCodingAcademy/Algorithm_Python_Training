nums = [1, 2, 2, 2, 3]

dp = [1] * len(nums)
prev = [-1] * len(nums)

# Build dp and prev
for i in range(len(nums)):
    for j in range(i):
        if nums[j] < nums[i] and dp[j] + 1 > dp[i]:
            dp[i] = dp[j] + 1
            prev[i] = j

# Find the end of the LIS
max_length = max(dp)
end_index = dp.index(max_length)

# Reconstruct LIS using your preferred loop
result_lst = [end_index]

while True:
    prev_index = prev[end_index]
    
    if prev_index == -1:
        break
    
    result_lst.append(prev_index)
    end_index = prev_index

# Reverse the order to correct direction
result_lst.reverse()

# Print one LIS
for idx in result_lst:
    print(nums[idx])
