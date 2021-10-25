
def fibonacci():
    a, b = 1, 1
    while True:
        yield b
        a, b = b, a + b


def digitzer():
    i = 1
    for num in fibonacci():
        i += 1
        digits = len(str(num))
        if digits == 1000:
            return i


print(digitzer())
