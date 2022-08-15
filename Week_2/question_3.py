def pascalPrincipal(frac_1, frac_2):
  n_1, d_1 = [int(i) for i in frac_1.split("/")]
  n_2, d_2 = [int(i) for i in frac_2.split("/")]
  return True if n_1 / d_1 == n_2 / d_2 else False

f_1, f_2 = input("Enter two fractions : ").split()
print("Pascal's fractions") if pascalPrincipal(f_1, f_2) else print("Not Pascal's fractions.")