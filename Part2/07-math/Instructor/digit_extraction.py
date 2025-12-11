num = 789

digits = []

while True:
    remainder = num % 10
    digits.append(remainder)
    num = num // 10
    if num == 0:
        break
    
print(digits)

