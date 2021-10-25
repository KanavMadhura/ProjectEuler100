from math import log as ln
from problem3 import is_prime


def upper_bound(n):
    # return the upper bound of the nth prime
    return n * (ln(n) + ln(ln(n)))


def lower_bound(n):
    # return the upper bound of the nth prime
    return n * (ln(n) + ln(ln(n)) - 1)


def find_prime(n):
    # return the nth prime
    for i in range(int(lower_bound(n)), int(upper_bound(n)) + 1):
        if is_prime(i):
            return i


if __name__ == '__main__':
    print(find_prime(10001))
