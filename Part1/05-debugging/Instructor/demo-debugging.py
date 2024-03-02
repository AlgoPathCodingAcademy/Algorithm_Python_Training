print("Simple Calculator")

# Getting user input
operation = input("Choose an operation (add, subtract, multiply): ")
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Performing calculations
if operation == "add":
    result = a + a
elif operation == "subtract":
    result = a - b
else:
    result = a * a

print(f"The result is: {result}")


    
