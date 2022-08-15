s = 0
c = 0

while True:
    n = int(input("Please enter a number: (0 to end) "))
    if n == 0:
        if c == 0:
            print("You've entered zero before anything.")
            continue
        else:
            print("End of the numbers.")
            break
    else:
        s += n
        c += 1

avg = s / c
print(f"Average = {avg}")