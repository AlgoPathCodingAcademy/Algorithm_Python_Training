matrix = [
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
    ]
    
target = 3

# largest index < target
# bisect upperbound
def findTargetRow(matrix,target):
    left = 0
    right = len(matrix)
    
    while True:
        if left >= right:
            return left
            
        mid = (left + right)//2
        
        if matrix[mid][0] > target:
            right = mid
        else:
            left = mid + 1

def findColumn(matrix,target):
    import bisect
    index = findTargetRow(matrix,target)
    if index == 0:
        return False

    # Now we find the largest index <= target
    index = index - 1

    column_index = bisect.bisect_left(matrix[index],target)
    if column_index < len(matrix[index]) and \
        matrix[index][column_index] == target:
        return True
    else:
        return False

def search_matrix(matrix, target):
    return findColumn(matrix,target)
    
print(search_matrix(matrix,target))
