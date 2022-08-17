# newton's method of square root
x = float(input("Enter a number: "))
guess = x / 2

while abs((guess * guess) - x) >= 10e-12:
    guess = (guess + (x / guess)) * 0.5

print(f"The square root is {guess}")