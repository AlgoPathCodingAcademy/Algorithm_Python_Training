input_list = [31,29,15,19,23,7,9,5,2]
# Substep in the insertion sort algorithm:
# 'index' refers to the position of the element selected for insertion.
# This substep locates the proper insertion point for the element by moving leftward
# through 'input_list' until it finds an element smaller than the one being inserted.
# The element at 'index' is then inserted immediately after the smaller element found.
# 'input_list' is the list being sorted
def insertNumberWithGap(index,gap,input_list):
    number = input_list[index]
    #print(range(index-gap,-1,-gap))
    for i in range(index-gap,-1,-gap):
        #print(number, " compare with ", input_list[i])
        if number < input_list[i]:
            #print("shift ", i, " to ", i+gap )
            input_list[i+gap] = input_list[i]
            #print(input_list)
            if i - gap <= 0:
                input_list[i] = number
            #print(input_list)
        else:
            input_list[i+gap] = number
            break

#Basic Test
insertNumberWithGap(5,4,input_list)
print(input_list)

gap = len(input_list)//2
while True:
    if gap == 0:
        break

    for index in range(gap,len(input_list)):
        insertNumberWithGap(index,gap,input_list)

    gap = gap//2
print(input_list)
