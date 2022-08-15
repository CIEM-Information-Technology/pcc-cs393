mass = int(input("Enter Mass :"))
velocity = int(input("Enter Velocity :"))
height = int(input("Enter Height :"))

# gravitational constant
g = 9.8

K_E = 0.5 * mass * (velocity ** 2)
P_E = mass * g * height

print(f"KE = {K_E}J, PE = {P_E}J")