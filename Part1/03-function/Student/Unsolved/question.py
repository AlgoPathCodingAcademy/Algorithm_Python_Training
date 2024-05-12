#Create a function named multiply that takes two numbers as arguments and returns their product.

#Write a function named is_even that checks if a given number is even.
#The function should return True if the number is even, and False otherwise.

#Write a Function to Find the Maximum of two Numbers

#Note: This is the exercise to understand the function could have no return value
#and also could have no input parameters
#Create a function called hello_message to print hello world

#Note: This is the exercise to undertand the function could have no return value
#Create a function called welcome_message that takes a person's name
#as an argument and prints a personalized welcome message.


#Create a function named activity_recommendation that takes one parameter:
#the type of weather (as a string). The function should recommend different activities based on the weather conditions.

#Task:
#If it's sunny, recommend "It's a great day for a hike."
#If it's raining, recommend "Perfect day for indoor games."
#If it's snowy, recommend "Good day for skiing."

#TODO convert the following code by using function calculate_distance
import math

#test input
#x1 = 0 
#y1 = 0
#x2 = 4
#y2 = 3

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
print("The distance between the two points is ", distance)

#TODO-Add your function calculate_distance here, call the function
# and get the distance between the two points


#What is the output of the following code ?
#Could you change the code to make it output the expected result
def print_greeting(name):
    print("Hello, " + name + "!")

# Calling the function
result = print_greeting("Alice")
print("The return value of print_greeting is:", result)



#Nested if else question
#Create a function named activity_recommendation that takes two parameters: the type of weather (as a string) and the temperature (as an integer).
#The function should recommend different activities based on the weather conditions and temperature.
#Task:
#If it's sunny and the temperature is above 25 degrees Celsius, recommend "It's a great day for a swim."
#If it's sunny and the temperature is 25 degrees or below, recommend "Perfect weather for a bike ride."
#If it's raining, regardless of temperature, recommend "Good day for visiting a museum."
#If it's snowy and the temperature is 0 degrees or below, recommend "How about building a snowman?"
#If it's snowy and above 0 degrees, recommend "Ideal weather for a snowball fight."
