def processed(list,threshold):
    num_bigger = 0
    for i in range(len(list)):
        if int(list[i]) > threshold:
            num_bigger = num_bigger + 1
    return len(list), num_bigger

input_parameters = input().split()
num = int(input_parameters[0])
threshold = int(input_parameters[1])

total_bigger = 0
while True:
    num_processed, num_bigger = processed(input().split(), threshold)
    num = num - num_processed
    #print(num)
    total_bigger = total_bigger + num_bigger
    if num <= 0:
        break
print(total_bigger)
