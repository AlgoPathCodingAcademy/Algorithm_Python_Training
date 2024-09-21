# Please sort the Person's age in ascending order
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

print("Before...")

for item in people:
    print(item.name)
    print(item.age)

def bubble_sort(object_array):
    n = len(object_array)
    # Traverse through all array elements
    for i in range(n-1):
        # Initialize the swap flag as False
        needSwap = False
        # Last i elements are already in place, no need to check them
        for j in range(n - 1 - i):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if object_array[j].age > object_array[j + 1].age:
                object_array[j], object_array[j + 1] = object_array[j + 1], object_array[j]
                needSwap = True
        # If no elements were swapped, break the loop
        if not needSwap:
            break

bubble_sort(people)

print("After...")

for item in people:
    print(item.name)
    print(item.age)
