m = int(input("Enter a number: "))
n = int(input("Enter another number: "))

d = m if m < n else n

while m % d != 0 or n % d != 0:
    d -= 1

print(f"GCD = {d}")