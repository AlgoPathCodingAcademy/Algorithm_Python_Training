'''
def is_number_consecutive(start, end, input_list):
    counter = 1
    for index in range(start+1,end+1):
        print(input_list[index], input_list[index-1])
        if input_list[index] == input_list[index-1] + 1:
            counter = counter + 1
            
    print("counter ", counter )
    if counter != 5:
        return False
    else:
        return True
'''

'''
        
def is_number_consecutive(start, end, input_list):
    is_consecutive = True
    for start in range(start, end):
        if input_list[start] + 1 != input_list[start+1]:
            is_consecutive = False
            
    return is_consecutive
'''

'''
def is_number_consecutive(start, end, input_list):
    counter = 1
    
    while True:
        if start >= end:
            break
        
        if input_list[start] + 1 == input_list[start+1]:
            counter = counter + 1
        
        start = start + 1    
        
    if counter == 5:
        return True
    else:
        return False
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
    
input_list = [1,3,4,5,6,7,10]

for index in range(0,len(input_list) - 4):
    print(is_number_consecutive(index,index+4,input_list))
