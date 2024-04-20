input_list = [1,2,6,7,8,9,10,20]
#More test cases
#input_list = [1,1,1,7,8,9,10,20]

#TODO use while loop
def is_number_consecutive(start, end, input_list):
    is_consecutive = True
    #TODO add your code

    return is_consecutive

print(is_number_consecutive(1,6,input_list)) #False
print(is_number_consecutive(2,7,input_list)) #True

is_consecutive = False
for i in range(len(input_list)-4):
    #check if numbers are consecutive
    is_consecutive = is_number_consecutive(i,i+4,input_list)
    
    #if not, return False
    if is_consecutive:
        break

print(is_consecutive)
