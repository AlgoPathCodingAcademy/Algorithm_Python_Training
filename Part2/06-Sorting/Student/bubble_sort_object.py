class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

for item in people:
    print(item.name, " : ", item.age)


# The bubble sort algorithm is given as below:
def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n-1):
        # Initialize the swap flag as False
        needSwap = False
        # Last i elements are already in place, no need to check them
        for j in range(n - 1 - i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                needSwap = True
        # If no elements were swapped, break the loop
        if not needSwap:
            break

#input_list = [7,6,5,4,3,2,1]
bubble_sort(people)
for item in people:
    print(item.name, " : ", item.age)



# TODO Please change the above bubble sort algorithm to sort the Person's age in ascending order
