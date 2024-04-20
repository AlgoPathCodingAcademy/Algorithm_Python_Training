input_list = [1,2,6,7,8,9,10,20]

#More test cases
#input_list = [1,1,1,7,8,9,10,20]

#Version 1
'''
#Test is_number_consecutive
#print(is_number_consecutive(0,4,input_list)) #False
#print(is_number_consecutive(2,6,input_list)) #True
def is_number_consecutive(start, end, input_list):
    if input_list[start+1] == input_list[start] + 1 and \
        input_list[start+2] == input_list[start+1] + 1 and \
        input_list[start+3] == input_list[start+2] + 1 and \
        input_list[start+4] == input_list[start+3] + 1:
        return True
    return False
'''
#add test case 
#print(is_number_consecutive(1,6,input_list)) #False
#print(is_number_consecutive(2,7,input_list)) #True
#Version 2: N consecutive numbers
#Use for loop
def is_number_consecutive(start, end, input_list):
    is_consecutive = True
    for start in range(start, end):
        if input_list[start] + 1 != input_list[start+1]:
            is_consecutive = False
            
    return is_consecutive

#Use while loop
'''
def is_number_consecutive(start, end, input_list):
    is_consecutive = True
    while True:
        if start + 1 > end:
            break

        if input_list[start] + 1 != input_list[start+1]:
            is_consecutive = False
            break

        start = start + 1

    return is_consecutive
'''

is_consecutive = False
for i in range(len(input_list)-4):
    #check if numbers are consecutive
    is_consecutive = is_number_consecutive(i,i+4,input_list)
    
    #if not, return False
    if is_consecutive:
        break

print(is_consecutive)
