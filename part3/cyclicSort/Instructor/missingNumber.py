n = int(input())
A = [int(x) for x in input().split()]

m = len(A)  # m should be n - 1

# Cyclic sort for values 1..m
for i in range(m):
    while True:
        value = A[i]

        # skip values that can't be placed (<=0 or > m)
        if value < 1 or value > m:
            break

        correct_index = value - 1

        if i == correct_index:
            break

        if A[i] == A[correct_index]:
            break

        A[i], A[correct_index] = A[correct_index], A[i]

# find the missing number
for i in range(m):
    if A[i] != i + 1:
        print(i + 1)
        break
else:
    # if all 1..m are in place, the missing one is n
    print(len(A) + 1)
