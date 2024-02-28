#NNCode 1125
start, elapsed = input().split()
new = int(start) + int(elapsed)

if int(new) > 6:
    my_new_new = int(new) % 7
    print(int(my_new_new))
else:
    print(int(new))
