m = float(input("Enter mass of the object:"))
v = float(input("Enter velocity of the object:"))
h = float(input("Enter height of the object:"))
g = 9.8

kinetic_energy = (m*(v**2))/2
potential_energy = m * g * h

print(f"K.E. = {kinetic_energy} J")
print(f"P.E. = {potential_energy} J")