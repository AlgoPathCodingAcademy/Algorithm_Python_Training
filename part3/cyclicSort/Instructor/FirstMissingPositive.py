#A = [1, 3, 6, 4, 1, 2]
#A = [-1, -3]

A = [1, 2, 6, 4, 3, 1]

for i in range(0,len(A)):
    while True:
        value = A[i]
        if value <= 0 or value > len(A) :
            break
        correct_index = value - 1
        
        if i == correct_index:
            # No change
            break
        
        if A[i] == A[correct_index]:
            # No change
            break
        
        A[i], A[correct_index] = A[correct_index],A[i]
        

value = 0

isHit = False
for i in range(len(A)):
    if i != A[i] - 1:
        value = i+1
        isHit = True
        break

if not isHit:
    value = len(A) + 1
    
print(value)
