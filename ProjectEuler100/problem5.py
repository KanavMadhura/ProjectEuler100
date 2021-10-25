# Euler Problem 5

# Only last 10 factors are necessary, since all integers 0-9
# are factors of integers 11-20
necessary_factors = [11, 12, 13, 14, 15, 16, 17, 18, 19]

# check for non-membership instead of membership to save time


def is_divisible(n):
    for i in necessary_factors:
        if n % i != 0:
            return False
    return True


# Start counter at 20. I could start it much later
# but that would save negligible time and may confuse readers
x = 20

# Set first result, loop through until confition is fulfilled,
# adding 20 each time since that way we don't need to check
# 20 in <<neccesary_factors>>
result = is_divisible(x)
while not result:
    x += 20
    result = is_divisible(x)
print(x)
# x == 232792560
# Could probably be optimised further
