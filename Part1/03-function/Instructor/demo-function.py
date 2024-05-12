#Example showing why function is useful
#Imagine a program where you need to greet users differently based on the time of day.
#Without using functions, your code might look something like this:
#The following code shows without function

# Variables for user names and the current hour
name1 = "Alice"
hour1 = 9
name2 = "Bob"
hour2 = 14
name3 = "Charlie"
hour3 = 20

# Greeting Alice
if hour1 < 12:
    print("Good morning, " + name1 + "!")
elif hour1 < 18:
    print("Good afternoon, " + name1 + "!")
else:
    print("Good evening, " + name1 + "!")

# Greeting Bob
if hour2 < 12:
    print("Good morning, " + name2 + "!")
elif hour2 < 18:
    print("Good afternoon, " + name2 + "!")
else:
    print("Good evening, " + name2 + "!")

# Greeting Charlie
if hour3 < 12:
    print("Good morning, " + name3 + "!")
elif hour3 < 18:
    print("Good afternoon, " + name3 + "!")
else:
    print("Good evening, " + name3 + "!")

#The following code shows use function
def greet(name, hour):
    if hour < 12:
        return "Good morning, " + name + "!"
    elif hour < 18:
        return "Good afternoon, " + name + "!"
    else:
        return "Good evening, " + name + "!"

# Using the function
print(greet("Alice", 9))    # Morning greeting
print(greet("Bob", 14))     # Afternoon greeting
print(greet("Charlie", 20)) # Evening greeting



def circle_area(radius):
    pi = 3.14159
    return pi * radius * radius

print(circle_area(5))

radius_input = float(input("Enter the radius of the circle: "))
area = circle_area(radius_input)
print("The area of the circle with radius {radius_input} is", area)

answer_value = 5
guessed_value_loop = int(input("Guess a value loop\n"))

'''
while (guessed_value_loop != answer_value):
    if guessed_value_loop > answer_value:
        print("Too big loop")
    elif guessed_value_loop < answer_value:
        print("Too small")
    
    guessed_value_loop = int(input("Guess a value loop\n"))
print("Correct")
'''
def checkInputValueSame(inputValue, answer_value):
    isSame = False
    if guessed_value_loop > answer_value:
        print("Too big loop")
    elif guessed_value_loop < answer_value:
        print("Too small")
    else:
        isSame = True

    return isSame

while (checkInputValueSame(guessed_value_loop, answer_value) != True):
    guessed_value_loop = int(input("Guess a value loop\n"))
print("Correct")




