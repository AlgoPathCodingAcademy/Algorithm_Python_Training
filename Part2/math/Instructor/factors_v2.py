def get_factors(num):
    if num == 1:
        return [1]

    factors = []
    factor = 1

    while factor * factor <= num:
        if num % factor == 0:
            factors.append(factor)

            # Add the paired divisor if different
            if factor * factor != num:
                factors.append(num // factor)

        factor += 1

    return factors
