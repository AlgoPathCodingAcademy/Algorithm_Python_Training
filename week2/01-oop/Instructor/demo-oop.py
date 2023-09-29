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

# Module
#https://trinket.io/turtle
#https://docs.python.org/3/library/turtle.html
#import turtle
#turtle =  turtle.Turtle()
#turtle.forward(100)
