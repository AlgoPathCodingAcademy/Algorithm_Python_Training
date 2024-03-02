
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




