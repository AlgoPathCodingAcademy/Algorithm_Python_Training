# Given funciton def insertNumber(index,input_list):
# This function completes a key substep in the insertion sort algorithm:
# 'index' refers to the position of the element selected for insertion.
# This substep locates the proper insertion point for the element by moving leftward
# through 'input_list' until it finds an element smaller than the one being inserted.
# The element at 'index' is then inserted immediately after the smaller element found.
# 'input_list' is the list being sorted

def insertNumber(index,input_list):
    number = input_list[index]
    while True:
        
        if index > 0 and input_list[index-1] > number:
            input_list[index] = input_list[index-1]
        else:
            input_list[index] = number
            break
        
        index = index - 1

input_list = [23,29,15,19,31,7,9,5,2]

#Test
insertNumber(1,input_list)
print(input_list) #should be [23, 29, 15, 19, 31, 7, 9, 5, 2]
insertNumber(2,input_list)
print(input_list) #should be [15, 23, 29, 19, 31, 7, 9, 5, 2]
insertNumber(3,input_list)
print(input_list) #should be [15, 19, 23, 29, 31, 7, 9, 5, 2]
insertNumber(4,input_list)
print(input_list) #should be [15, 19, 23, 29, 31, 7, 9, 5, 2]
insertNumber(5,input_list)
print(input_list) #should be [7, 15, 19, 23, 29, 31, 9, 5, 2]
insertNumber(6,input_list)
print(input_list) #should be [7, 9, 15, 19, 23, 29, 31, 5, 2]
insertNumber(7,input_list)
print(input_list) #should be [5, 7, 9, 15, 19, 23, 29, 31, 2]
insertNumber(8,input_list)
print(input_list) #should be [2, 5, 7, 9, 15, 19, 23, 29, 31]

#Add loop on top of function
for i in range(0, len(input_list)):
    insertNumber(i, input_list)
print("Sorted list ", input_list)
