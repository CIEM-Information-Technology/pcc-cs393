def properDivisor(n: int):
    divisors = []
    for i in range(1, n):
        if n % i == 0:
            divisors.append(i)
    return divisors

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    proper_divisors = properDivisor(n)
    print("Proper divisors of n are ", proper_divisors)