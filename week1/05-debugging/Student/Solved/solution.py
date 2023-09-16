for i in range(1, 6):
    for j in range(i):
        print(j+1, end=' ')
    print()

print("Answer...")

i = 1
while i < 5:
    j = 0
    while (j < i):
        print(j+1, end=' ')
        j = j + 1
    print()
    i = i + 1
