from math import sqrt, ceil


def is_prime(n):
    for i in range(3, ceil(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


sum = 2 + 3 + 5 + 7
for i in range(9, 2000000, 2):
    if is_prime(i):
        sum += i

print(sum)
