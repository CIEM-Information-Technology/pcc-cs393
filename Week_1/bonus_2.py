# fraction_add.py

frac_1 = input("Enter first fraction: ")
frac_2 = input("Enter second fraction: ")

n_1 = int(frac_1.split("/")[0])
d_1 = int(frac_1.split("/")[1])

n_2 = int(frac_2.split("/")[0])
d_2 = int(frac_2.split("/")[1])

n_r = str((n_1 * d_2) + (n_2 * d_1))
d_r = str(d_1 * d_2)

r = "/".join([n_r, d_r])

print(f"Result = {r}")
