
def collatz(n):
    if n % 2 == 0:
        # print(n / 2)
        return n / 2
    else:  # n is odd
        # print(3*n + 1)
        return 3*n + 1


cache = {}


def collatz_recursive(n):
    if n not in cache:
        if n == 1:
            cache[n] = 1
        elif n % 2 == 0:
            cache[n] = collatz_recursive(n // 2) + 1
        else:  # n is odd
            cache[n] = collatz_recursive(3*n + 1) + 1
    return cache[n]


if __name__ == "__main__":
    rmax = 0
    for i in range(1, 1000001):
        cmax = collatz_recursive(i)
        if rmax < cmax:
            rmax = cmax
    print(rmax)
