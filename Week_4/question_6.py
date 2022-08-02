def calculateGcd(m, n):
    d = m if m < n else n

    while m % d != 0 or n % d != 0:
        d -= 1

    return d


def reduceFraction(numerator: int, denominator: int):
    gcd = calculateGcd(numerator, denominator)
    return (int(numerator/gcd), int(denominator/gcd))


if __name__ == '__main__':
    n, d = input("Enter numberator and denominator: ").split()
    n, d = reduceFraction(int(n), int(d))
    print(f"Reduced Fraction = {n}/{d}")
