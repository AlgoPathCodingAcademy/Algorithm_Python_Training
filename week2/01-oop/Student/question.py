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
#Use the turtle class to draw a square, each side has 200 steps

#TODO
#Read the documentation of list in the following
#https://python-reference.readthedocs.io/en/latest/docs/list/
#To answer the following question
#How many ways the list object can be created
#Give some methods of list class
#Give example of creating a list and uses one of methods you find in the documentation
