from question_2 import checkPrime


def nextPrime(num):
    n = num + 1
    while True:
        if checkPrime(n):
            return n
        else:
            n += 1


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    next_prime = nextPrime(n)
    print(f"Next prime number is : {next_prime}")
