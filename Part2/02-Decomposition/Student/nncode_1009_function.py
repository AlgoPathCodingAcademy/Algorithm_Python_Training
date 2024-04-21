#input
#list: A list of numeric values (integers or floats).
#This list contains the elements that need to be evaluated against a specified threshold.
#threshold: A numeric value (integer or float) that serves as the benchmark for comparison.
#Elements in the list will be compared to this value to determine if they exceed it.

#output
#Returns two values:
#First value (int): The total number of elements processed. This is essentially the length of the list.
#Second value (int): The number of elements in the list that exceed the specified threshold.
#TODO implement this function
def processed(list,threshold):
    pass    

input_parameters = input().split()
num = int(input_parameters[0])
threshold = int(input_parameters[1])

total_bigger = 0
while True:
    num_processed, num_bigger = processed(input().split(), threshold)
    num = num - num_processed
    #print(num)
    total_bigger = total_bigger + num_bigger
    if num <= 0:
        break
print(total_bigger)

