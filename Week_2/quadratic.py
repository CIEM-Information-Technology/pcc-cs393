import math as m

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))
c = int(input("Enter the value of c: "))

d = (b**2) - (4*a*c)
root_1 = (-b + m.sqrt(d))/(2*a)
root_2 = (-b - m.sqrt(d))/(2*a)

print(f"R1 = {root_1}, R2 = {root_2}")

if d < 0:
    print("Roots are not real.")
else:
    print("Roots are real.")
