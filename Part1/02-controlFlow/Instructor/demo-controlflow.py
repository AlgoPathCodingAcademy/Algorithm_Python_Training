
'''
#Selection
#if condition
test_input_choice = int(input("Your choice\n"))
#if test_input_choice == 2:
#Or
if (test_input_choice == 2):
    print("Correct!")
else:
    print("Incorrect!")

#multi if condition
guessed_value = int(input("Guess a value\n"))
answer_value = 5
if (guessed_value > answer_value):
    print("Too big")
elif (guessed_value == answer_value):
    print("Correct")
else:
    print("Too small")

#Sample code the calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

if operation == '+':
    print(str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif operation == '-':
    print(str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
elif operation == '*':
    print(str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
elif operation == '/':
    if num2 != 0:
        print(str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
    else:
        print("Division by zero is not allowed.")
else:
    print("Invalid operation")

#Iteration:
#Add some repetition:

#While loop - variance 1
guessed_value_loop = int(input("Guess a value loop\n"))

while (guessed_value_loop != answer_value):
    if guessed_value_loop > answer_value:
        print("Too big loop")
    elif guessed_value_loop < answer_value:
        print("Too small")
    
    guessed_value_loop = int(input("Guess a value loop\n"))
print("Correct")

#While loop - variance 2
while (True):
    guessed_value_loop = int(input("Guess a value loop variance - break\n"))
    if (guessed_value_loop > answer_value):
        print("Too big")
    elif (guessed_value_loop < answer_value):
        #Break from Iteration:
        print("Too small")
    else:
        print("Correct")
        break

#A for loop is used for iterating over a sequence (that is either a list, or a string).
#This is less like the for keyword in other programming languages, and works more like
# an iterator method as found in other object-orientated programming languages.
#For loop - string, list, range()
#Object must be iterable
for i in "abc":
    print(i)

for i in [7,8, "a"]:
    print(i)

for i in range(5):
    print(i)

#Check if the object is iterable
#for i in 6:
#    print(i)
'''

#Multi-loop

'''
#Multi-while loop
room_number = 2
secret_number = 5

while True:
    guessed_room = int(input("Guess a room (1, 2, or 3):\n"))

    if (guessed_room == 2):
        print("Correct room! Now, guess the secret number in this room.")
        while (True):
            guessed_value_new = int(input("Guess a value (between 1 and 10):\n"))
            if (guessed_value_new > secret_number):
                print("Too big")
            elif (guessed_value_new < secret_number):
                #Break from Iteration:
                print("Too small")
            else:
                print("Correct")
                break
        #Important! it exits the inner loop
        break
    else:
        print("Wrong room, try again.")
'''

'''
#Multi-while loop
#*
#**
#***
#****
#*****
output_str = ""
lines = 0
while (lines < 5):
    lines = lines + 1
    linesStar = 0
    while (linesStar < lines):
        output_str = output_str + "*"
        linesStar = linesStar + 1
    output_str = output_str + "\n"
print(output_str)
'''

#Multi-for loop
output_str_for = ""
for line in range(1,6):
    for startPerLine in range(line):
        output_str_for = output_str_for + "*"
    output_str_for = output_str_for + "\n"
print(output_str_for)




    
