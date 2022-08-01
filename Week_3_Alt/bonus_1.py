from math import floor


n = int(input("Enter a positive integer: "))
l = n

while l != 1:
    if l % 2 == 0:
        print(f"{l} ", end="")
        l = floor(l / 2)
    else:
        print(f"{l} ", end="")
        l = (l * 3) + 1
else:
    print("1 \n")