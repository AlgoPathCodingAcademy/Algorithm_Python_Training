#TODO
#Question 1: Is Dog a class or object
#Question 2: What is __init__ called ?
#Question 3: What are bark and display_age called ?

class Dog:
    # Initializer (constructor) method
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method to make the dog bark
    def bark(self):
        return "Woof!"

    # Method to display the dog's age
    def display_age(self):
        return f"{self.name} is {self.age} years old."

#TODO
#Please write a example of how to use Dog class

#TODO See the following code
#Question: Please correct the errors of the following code
#It should print the total number of books is 2

#TODO
#Question: After the error is fixed, please use 2 ways to change
#the author of book 1, which way do you think.
class Book:
    # Class attribute
    total_books = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        total_books = total_books + 1

    def set_details(self, title, author):
        self.title = title
        self.author = author

    def display_details(self):
        print("Title: ", self.title, "Author: " ,self.author)

    def display_total_books():
        print("Total books: ", total_books)

# Usage:
book1 = Book("1984", "George Orwell")
book2 = Book("Brave New World", "Aldous Huxley")


book1.display_details()             # Output: Title: 1984, Author: George Orwell
book2.display_details()             # Output: Title: Brave New World, Author: Aldous Huxley

book2.set_details("To Kill a Mockingbird", "Harper Lee")
book2.display_details()             # Output: Title: To Kill a Mockingbird, Author: Harper Lee

Book.display_total_books()          # Output: Total books: 2

#TODO
#Correct the following error program:
'''
class Student:
    total_students = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        total_students += 1

    # Instance method to display student info
    def display_info(self):
        return f"Student Name: {name}, Age: {age}, Grade: {grade}"

    # Class method to show the total number of students
    @classmethod
    def show_total_students(cls):
        return cls.total_students

    # Static method to determine if the grade is passing
    @staticmethod
    def is_passing(grade):
        if grade >= 50:
            return True
        return False

# Test the class:
s1 = Student("Alice", 20, 65)
print(s1.display_info())
print(Student.is_passing(s1.grade))
print(Student.show_total_students())
'''

#TODO
#Complete the following task
# Imagine you're developing a system for a school to manage its students. Please create a Student class with the following requirements:
# Instance Attributes:
# name: Represents the student's name.
# age: Represents the student's age.
# grade: the student's grades.
# Instance Method:
# add_grade(grade): Adds this student's grade to the system.
# Class Attribute:
# school_name: Represents the name of the school. Initially set to "Unnamed School".
# Class Method:
# set_school_name(new_name: str): Sets the name of the school.
# average_grade(): Returns the average grade of whole student.
# Static Method:
# is_passing_grade(grade: float) -> bool: Returns True if the grade is 50 or above, otherwise returns False.

#TODO
# You're developing software for a zoo. 
# Animals at the zoo have general attributes (like name, species, and age) and general behaviors (like speak and eat).
# Different types of animals have some species-specific behaviors. For instance:
# Birds can fly.
# Fish can swim.
# Given the Animal Base class as follows, create two children(sub) class named Bird and Fish that inherit from Animal.
# Add species-specific behaviors to the derived classes.
# For bird class, 1. add fly method 2. overide speak method of base class
# For fish class, 1. add swim method 2. overide spake method of base class
class Animal:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def speak(self):
        pass

    def eat(self, food):
        return f"{self.name} eats {food}."

#TODO
#Looking into https://github.com/pyGuru123/Python-Games/blob/master/Aeroblasters/main.py
#1. List the external Python modules it uses
#2. List few external Python classes it uses
#3. In Line 36: pygame.image.load('Assets/plane.png'), what is image in this context ?
#4. In Line 183: is update() a class method or instance method or static method (tap_to_play_msg.update())

#TODO
#Use the Turtle class (class turtle.Turtle) to draw a square, each side has 200 steps
# Module
#https://trinket.io/turtle
#Please pay attention to the following mentioned in the link above for eaysier understanding
#Methods of RawTurtle/Turtle and corresponding functions¶
#Most of the examples in this section refer to a Turtle instance called turtle.
#https://docs.python.org/3/library/turtle.html
#import turtle

#TODO
#Look into Python Fraction moudle and try to figure out using this Fraction module to 
#create fraction addition and print the result. Part of the code is listed as below:

#import fractions
#TODO please complete the following code to create
# two Fraction objects.
# Define two fractions
#f1 = ?  # Represents 1/4
#f2 = ?  # Represents 2/3
# Add the fractions
#result = f1 + f2
#print(result)  # 11/12

#TODO
#Read the documentation of list in the following
#https://python-reference.readthedocs.io/en/latest/docs/list/
#To answer the following question
#How many ways the list object can be created
#Give some methods of list class
#Give example of creating a list and uses one of methods you find in the documentation

#Local variable, Enclosing variable and Global variable
#TODO
#What's the final output of the following code ?
'''
def local_example():
    x = 10
    print("Inside function:", x)

local_example()
print("Outside function:", x)
'''
#What's the final output of the following code ?
y = 20
def global_example():
    global y
    print("Inside function (before change):", y)
    y = 30
    print("Inside function (after change):", y)

global_example()
print("Outside function:", y)

#What's the final output of the following code ?
def outer():
    z = 40
    def inner():
        nonlocal z
        print("Inside inner (before change):", z)
        z = 50
        print("Inside inner (after change):", z)
    inner()
    print("Inside outer:", z)

outer()

#What's the final output of the following code?
a = 100

def first_function():
    a = 200
    def second_function():
        nonlocal a
        a = 300
    second_function()
    print("Inside first_function:", a)

first_function()
print("Global scope:", a)


#Mutable vs immutable
#TODO
#What's the final value of items ? Why ? 
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("apple"))
print(add_item("banana"))

#TODO
#What's the final value of s ? Why ?
s = "world"
print(f"Original string: {s}, id: {id(s)}")

s = "Hello " + s
print(f"String after concatenation: {s}, id: {id(s)}")
