class car:
    def __init__(self,model,color,safeToDrive):
        self.model = model
        self.color = color
        self.safeToDrive = safeToDrive
   
    def showMeYourColor(self):
        print("Ok, color is ", self.color)
   
    def isOkToDrive(self):
        if (self.safeToDrive):
            print("Safe to Drive")
        else:
            print("No")
       

myCar = car("BMW","black", True)
myCar.isOkToDrive()

yourCar = car("Toy", "Red", False)
yourCar.isOkToDrive()


class Calculator:
    def __init__(self):
        pass

    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

# Usage:
calc = Calculator()
print(calc.add(5, 3))        # Output: 8
print(calc.multiply(5, 3))  # Output: 15

class Dog:
    # Class attribute
    legs = 4

    # Initializer (constructor) method
    def __init__(self, name, age):
        # Object attributes (instance attributes)
        self.name = name
        self.age = age

    # Method to display species
    def display_legs():
        print("Dog has ", Dog.legs, " legs")

# Usage:

# Create instances of the Dog class
buddy = Dog(name="Buddy", age=5)
charlie = Dog(name="Charlie", age=3)

# Access class attribute using the class name
print(Dog.legs)            # Output: 4
print(Dog.display_legs())

# Access class attribute using an instance
print(buddy.legs)          # Output: 4
print(charlie.legs)        # Output: 4

# Access object attributes using the instances
print(buddy.name)             # Output: Buddy
print(charlie.age)            # Output: 3

# Module
#https://trinket.io/turtle
#https://docs.python.org/3/library/turtle.html
#import turtle
#turtle =  turtle.Turtle()
#turtle.forward(100)
