lst = [38,27,43,3,9,82,10]

def merge(left,right):
    start_point_left = 0
    start_point_right = 0
    result = []
    
    if len(left) == 0:
        return right
        
    if len(right) == 0:
        return left
    
    while True:
        if left[start_point_left] <= right[start_point_right]:
            result.append(left[start_point_left])
            start_point_left += 1
        else:
            result.append(right[start_point_right])
            start_point_right += 1
    
        if start_point_left == len(left):
            for index in range(start_point_right,len(right)):
                result.append(right[index])
            break
                
        if start_point_right == len(right):
            for index in range(start_point_left,len(left)):
                result.append(left[index])
            break
            
    return result
    
left = [3,27,38,43]
right = [3,10,82]

result = merge(left,right)
print("Test merge process", result)

        
def mergeSort(lst):
    if len(lst) <= 1:
        return lst
        
    sort_part_left = mergeSort(lst[:len(lst)//2])
    sort_part_right = mergeSort(lst[len(lst)//2:])
    
    return merge(sort_part_left,sort_part_right)
    

output = mergeSort(lst)
print("Test merge sort process",output)
