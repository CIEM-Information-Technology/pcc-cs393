n_1, d_1 = input("Enter a fraction : ").split("/")
n_2, d_2 = input("Enter another fraction : ").split("/")

n_1, n_2, d_1, d_2 = int(n_1), int(n_2), int(d_1), int(d_2)
r = [
     str((n_1 * d_2) + (n_2 * d_1)),
     str(d_1 * d_2)
]
print("The result is " + "/".join(r))