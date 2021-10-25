
cache = {}


def fibonacci(n):
    # return the n-th term of the Fibonacci sequence

    # use cache to store values
    if n in cache:
        return cache[n]

    # recursive sequence
    if n == 1:
        value = 1
    elif n == 2:
        value = 1
    else:  # n > 2
        value = fibonacci(n - 1) + fibonacci(n - 2)

    # store value in cache
    cache[n] = value
    return value


sum = 0
for i in range(1, 34):
    num = fibonacci(i)
    if num % 2 == 0:
        sum += num
print(sum)
