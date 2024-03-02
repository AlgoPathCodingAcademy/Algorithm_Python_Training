import random

#Class basic
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

#=============Attribute=============
#Access object's (instance's) attribute
#Two ways:
#1.Directly access
#2.Use method

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
    # Bad Design because of inheritance
    def display_legs():
        print("Dog has ", Dog.legs, " legs")

    #@classmethod
    #def display_legs(cls):
    #    print(cls.__name__, "has ", Dog.legs, " legs" )

    @classmethod
    def change_legs(cls,num_of_legs):
        Dog.legs = num_of_legs
        
    @staticmethod
    def isGoodName(name):
       pass

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

# Access object/instance attributes using the instances
print(buddy.name)             # Output: Buddy
print(charlie.age)            # Output: 3


#=============Method=============
class VideoGame:
    default_platform = "PC"  # Class attribute: Default platform for all games

    def __init__(self, title, genre):
        self.title = title  # Instance attribute: Game title
        self.genre = genre  # Instance attribute: Game genre

    # Instance method: Displays game's details
    def display_details(self):
        return f"Title: {self.title}, Genre: {self.genre}, Platform: {VideoGame.default_platform}"

    # Class method: Change the default platform for all games
    @classmethod
    def set_default_platform(cls, platform):
        cls.default_platform = platform

    # Static method: Check if a game title follows naming convention (no special characters)
    @staticmethod
    def is_valid_title(title):
        return title.isalnum()  # True if title has only alphanumeric characters, False otherwise

# Testing
game1 = VideoGame("SuperFunGame", "Adventure")
print(game1.display_details())  # Output: Title: SuperFunGame, Genre: Adventure, Platform: PC

VideoGame.set_default_platform("PS5")
game2 = VideoGame("AnotherFunGame", "Racing")
print(game2.display_details())  # Output: Title: AnotherFunGame, Genre: Racing, Platform: PS5

print(VideoGame.is_valid_title("Game#3"))  # Output: False
print(VideoGame.is_valid_title("Game3"))   # Output: True

#=============Inheritance=============
class car:
    def __init__(self,model,color,safeToDrive):
        self.model = model
        self.color = color
        self.safeToDrive = safeToDrive
   
    def showMeYourColor(self):
        print("Ok, color is ", self.color)

    def refuel(self):
        print("Refilling the ", self.model ," with gasoline.")

    def isOkToDrive(self):
        if (self.safeToDrive):
            print("Safe to Drive")
        else:
            print("No")
       
class electrical_car(car):
    def __init__(self, model, color, safeToDrive, battery_power):
        super().__init__(model, color, safeToDrive)
        self.battery_power = battery_power
        
    def getBatteryPower(self):
        return self.battery_power
        
    def setBatteryPower(self, power):
        self.battery_power = power
        
    def refuel(self):
        print("Recharging the ", self.model ,"'s battery")

eCar = electrical_car("tesla", "red", "yes", 90)
#eCar.setBatteryPower(20)
bPower = eCar.getBatteryPower()
print(bPower)

eCar.refuel()

#Last example to explain @classmethod
class GermanShepherd(Dog):
    pass

GermanShepherd.display_legs() 

# Module
#from car import my_car
import car
#print(car.__file__)
my_car_instance = car.my_car("BMW","black", True)
my_car_instance.isOkToDrive()

from car_electric_car import my_electrical_car
eCar = electrical_car("tesla", "red", "yes", 90)
#eCar.setBatteryPower(20)
bPower = eCar.getBatteryPower()
print(bPower)

eCar.refuel()

from car_electric_car import my_car_aliases as ec
my_car_instance = ec("BMW","black", True)
my_car_instance.isOkToDrive()

import car as mc
my_car_instance = mc.my_car("BMW","black", True)
my_car_instance.isOkToDrive()

#Module
#Python random module
#https://docs.python.org/3/library/random.html
#Step 1. Where is random Python module 
import random
#print import module path
print(random.__file__)

#Step 2. Find what classes are available in the random Python module
# class random.Random
# class random.SystemRandom
# Looks not ideal(Can't be done by these two classes) by looking into the documentation

#Step 3. Any Module function available ?
# Directly call module function
# random.randint(a, b)
# Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1).
random_number = random.randint(1, 8)
print(random_number)
