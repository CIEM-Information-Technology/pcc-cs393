from math import floor

n = int(input("Enter a number to factorize: "))
if n <= 2:
    print("Enter a number greater than 2.")
    exit()

factor = 2

print(f"The prime factors of {n} are: ")
while factor <= n:
    if n % factor == 0:
        print(factor)
        n = floor((n/factor))
    else:
        factor += 1
