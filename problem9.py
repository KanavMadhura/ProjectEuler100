# Uses Euclid's Formula to construct Triples

def pythagorean_triple(m, n):
    return m**2 - n**2, 2*m*n, m**2 + n**2


def triple_sum_1000():
    a, b, c = 3, 4, 5
    # guessed range parameter. Started with 5 and went up by 10
    for i in range(25):
        # loop through each possible combination of integers
        for j in range(i):
            a, b, c = pythagorean_triple(i, j)
            # return product as per problem specifications
            if a + b + c == 1000:
                return a*b*c
    # Used for testing range parameter
    return('increase range!')


print(triple_sum_1000())
