#lst = [6,5,8,9,3,10,15,12,16]
lst = [10,5,8,12,15,6,3,9,16]
#lst = [10,10,10,10]

def quickSelect(lst):
    pivot = lst[0]
    start = 1
    end = len(lst)-1
    
    while True:
        
        while True:
            if start > end:
                break
            
            if lst[start] > pivot:
                break
            
            start = start + 1
            
        while True:
            if start > end:
                break
            
            if lst[end] < pivot:
                break
            
            end = end - 1
            
        if start > end:
            break
        
        lst[start],lst[end] = lst[end],lst[start]
        
    # Place the pivot
    lst[0],lst[end] = lst[end],lst[0]
        
            
quickSelect(lst)

print(lst)
