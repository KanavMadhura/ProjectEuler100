from math import sqrt


def find_factors(num):
    factors = []
    for i in range(1, int(sqrt(num)) + 1):
        if num % i == 0:
            factors.append(i)
            factors.append(num // i)
    return factors


def find_500():
    upper = 100
    n = 1
    for i in range(2, upper + 1):
        n += i
        if len(find_factors(n)) == 500:
            return n
    return "increase upper!"


print(find_500())
