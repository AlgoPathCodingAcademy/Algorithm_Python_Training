list_a = [3,5,8]
list_b = [2,8,9,10,15]

point_a = 0
point_b = 0

list_output = []

#Use For loop - Method 1
for _ in range(len(list_a) + len(list_b)):
    if point_a == len(list_a):
        for index in range(point_b,len(list_b)):
            list_output.append(list_b[index])
        break
            
    if point_b == len(list_b):
        for index in range(point_a,len(list_a)):
            list_output.append(list_a[index])
        break
        
    if list_a[point_a] < list_b[point_b]:
        list_output.append(list_a[point_a])
        point_a = point_a + 1
        continue
    elif list_a[point_a] > list_b[point_b]:
        list_output.append(list_b[point_b])
        point_b = point_b + 1
        continue
    else:
        list_output.append(list_a[point_a])
        list_output.append(list_b[point_b])
        point_a = point_a + 1
        point_b = point_b + 1
        continue
    
print(list_output)

#Use While loop - Method 2
point_a = 0
point_b = 0

list_output = []

while True:
    if list_a[point_a] < list_b[point_b]:
        list_output.append(list_a[point_a])
        point_a = point_a + 1
    elif list_a[point_a] > list_b[point_b]:
        list_output.append(list_b[point_b])
        point_b = point_b + 1
    else:
        list_output.append(list_a[point_a])
        list_output.append(list_b[point_b])
        point_a = point_a + 1
        point_b = point_b + 1
        
    if point_a == len(list_a):
        for index in range(point_b,len(list_b),1):
            list_output.append(list_b[index])
        break
            
    if point_b == len(list_b):
        for index in range(point_a,len(list_a),1):
            list_output.append(list_a[index])
        break

print(list_output)
