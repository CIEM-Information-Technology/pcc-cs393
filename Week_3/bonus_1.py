from math import floor


num = int(input("Enter a positive integer: "))
last_num = num

while last_num != 1:
    if last_num % 2 == 0:
        print(f"{last_num} ", end="")
        last_num = floor(last_num / 2)
    else:
        print(f"{last_num} ", end="")
        last_num = (last_num * 3) + 1
else:
    print("1 \n")
