#TODO Correct the following code to meet the requirement as described below:
#The program below aims to assist a user in planning activities for the day based on the weather. 
#The user provides input on whether it's rainy or sunny and whether it's a weekday or weekend. 
#The program should suggest an activity accordingly:
#Rainy + Weekday: "Work indoors."
#Rainy + Weekend: "Watch a movie at home."
#Sunny + Weekday: "Work outdoors."
#Sunny + Weekend: "Go to the beach."

print("Day Planner")

# Getting user input
weather = input("Is the weather rainy or sunny today? ")
day_type = input("Is today a weekday or weekend? ")

# Suggesting an activity
if weather == "rainy":
    if day_type == "weekday":
        suggestion = "Watch a movie at home."
    else:
        suggestion = "Work indoors."
elif weather == "sunny":
    if day_type == "weekday":
        suggestion = "Go to the beach."
    else:
        suggestion = "Work outdoors."
else:
    suggestion = "Invalid input. Please specify weather as 'rainy' or 'sunny' and day type as 'weekday' or 'weekend'."

print(f"Suggested activity: {suggestion}")