
rmax = 0
for i in range(1, 1000):
    for j in range(1, 1000):
        num = i*j
        if str(num) == str(num)[::-1] and rmax < num:
            rmax = num
print(rmax)
