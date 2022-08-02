def checkPrime(num):
    # implement error checking for numbers < 1
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
    return True


if __name__ == '__main__':
    n = int(input("Enter a number to check: "))
    print("Prime Number") if checkPrime(n) else print("Not a prime number")
