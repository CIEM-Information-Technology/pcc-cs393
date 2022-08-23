def proper_divisor(num: int):
    """
    find the proper divisors of a number
    :param num: a number of integer type
    :return: list of proper divisors
    """
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return divisors


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    proper_divisors = proper_divisor(n)
    print("Proper divisors of n are ", proper_divisors)
