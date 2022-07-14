
def energy_calculation_at_half_height(m, v):
    return (m * (v**2))

if __name__ == "__main__":
    m = float(input("Enter mass of the object: "))
    v = float(input("Enter velocity of the object: "))

    print(f"Kinetic Energy = Potential Energy = {energy_calculation_at_hal_height(m,v)}")
    
