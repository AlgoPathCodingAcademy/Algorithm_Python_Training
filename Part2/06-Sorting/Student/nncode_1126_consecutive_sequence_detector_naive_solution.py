#TODO just compare 5 consecutive numbers;
#You can assume the distance between start and end is always 4
#meaning the caller guarantees five numbers from start to end (included)
def is_number_consecutive(start, end, input_list):
    is_consecutive = True
    #TODO add your code
    return is_consecutive

print(is_number_consecutive(0,4,input_list)) #False
print(is_number_consecutive(2,6,input_list)) #True

is_consecutive = False
for i in range(len(input_list)-4):
    #check if numbers are consecutive
    is_consecutive = is_number_consecutive(i,i+4,input_list)

    #if not, return False
    if is_consecutive:
        break

print(is_consecutive)
