list_input= [64,25,12,22,11]

for i in range(len(list_input)):
    number = list_input[i]
    index = i
    for j in range(i+1,len(list_input)):
        if list_input[j] < number:
            number = list_input[j]
            index = j
    #print("Round ", i, "min_index ",index, "min_number ", number)
    if i != index:
        list_input[index],list_input[i] = list_input[i], list_input[index]

print(list_input)
