f_a, f_b = input("Enter two fractions : ").split(" ")[:2]
n_1, d_1 = [int(i) for i in f_a.split("/")]
n_2, d_2 = [int(i) for i in f_b.split("/")]
r = [
     str((n_1 * d_2) + (n_2 * d_1)),
     str(d_1 * d_2)
]
print("The result is " + "/".join(r))