
def is_prime(n):
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    num = 600851475143
    for i in range(2, num + 1):
        if is_prime(i) and num % i == 0:
            print(i)
