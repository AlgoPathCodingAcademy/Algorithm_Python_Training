list_input= [64,25,12,22,11]

def return_min_index(start, end, list):
    number = list[start]
    index = start
    for i in range(index+1, end+1):
        if list[i] < number:
            number = list[i]
            index = i
    #print(index,number)
    return index,number

return_min_index(0,len(list_input)-1,list_input) #answer 0 11
return_min_index(1,3,list_input) #answer 1 12
return_min_index(2,4,list_input) #answer 2 11
return_min_index(2,2,list_input) #answer 2 12

for i in range(len(list_input)):
    index,number = return_min_index(i,len(list_input)-1,list_input)
    #print(index,number)
    if i != index:
        list_input[i], list_input[index] = list_input[index],list_input[i]

print(list_input)
