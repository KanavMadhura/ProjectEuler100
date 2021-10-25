sum = 3
for x in range(4, 1000):
    if (x % 3 == 0) or (x % 5 == 0):
        sum += x
print(sum)
