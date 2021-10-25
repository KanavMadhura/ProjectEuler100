from math import factorial

counter = 0

for n in range(23, 101):
    for r in range(n + 1):
        if factorial(n) / (factorial(r) * factorial(n - r)) > 1000000:
            counter += 1
print(counter)
