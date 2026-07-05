# left smaller
 
lst = [1,7,9,5]

stack = []

result = [-1] * len(lst)

for i in range(len(lst)):
    
    while True:
        if len(stack) == 0:
            stack.append(lst[i])
            break
            
        top = stack[-1]
        
        # Get the answer
        if lst[i] > top:
            result[i] = top
            stack.append(lst[i])
            break
        
        stack.pop()
        
print(result)

# right smaller

stack = []

result = [-1] * len(lst)

for i in range(len(lst)):
    
    while True:
        if len(stack) == 0:
            stack.append((lst[i],i))
            break
        
        top,index = stack[-1]
        
        # Get the answer:
        if lst[i] < top:
            stack.pop()
            result[index] = lst[i]
            #continue
        else:
            stack.append((lst[i],i))
            break
            
print(result)
