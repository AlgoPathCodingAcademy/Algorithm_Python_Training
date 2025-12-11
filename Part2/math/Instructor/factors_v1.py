num = 24
factors = []

for num_ in range(1, int(num**0.5) + 1):
    if num % num_ == 0:
        factors.append(num_)              # small divisor
        pair = num // num_
        if pair != num_:
            factors.append(pair)          # large divisor

print(factors)
