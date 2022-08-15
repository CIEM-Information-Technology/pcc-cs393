from cmath import sqrt

def quadraticRoots(a, b, c):
  a, b, c = int(a), int(b), int(c)
  d = sqrt((b ** 2) - 4 * a * c)
  r_1 = (- b + d) / (2 * a)
  r_2 = (- b - d) / (2 * a)
  return [r_1, r_2]

a, b, c = input("Enter three a, b and c : ").split()
roots = quadraticRoots(a, b, c)
print(f"Roots are {roots[0]}, {roots[1]}")