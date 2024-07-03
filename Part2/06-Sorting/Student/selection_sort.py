list_input= [64,25,12,22,11]

for i in range(len(list_input)-1):
    number = list_input[i]
    index = i
    #TODO why do we need to use i+1 instead of i
    for j in range(i+1,len(list_input)):
        if list_input[j] < number:
            number = list_input[j]
            index = j
    #print("Round ", i, "min_index ",index, "min_number ", number)
    #TODO why do we need to check if i != index
    # You could uncomment the print above to help you.
    if i != index:
        #TODO what does this code do ? Could we write a function for it ?
        list_input[index],list_input[i] = list_input[i], list_input[index]

print(list_input)
