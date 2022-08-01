values = []

while True:
    n = float(input("Enter a value (enter 0 to end) : "))
    if n == 0:
        if len(values) == 0:
            print("You can't end before you begin.")
            continue
        elif len(values) > 0:
            print("This is the end!")
            break
    else:
        values.append(n)

s = 0
for i in values:
    s += i

average = s / len(values)
print(f"The average is {average}")