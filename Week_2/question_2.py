def greaterNumber(a, b):
  return a > b

n_1, n_2 = list(map(int, input("Enter two numbers: ").split()))
print(f"{n_1} is greater.") if greaterNumber(n_1, n_2) else print(f"{n_2} is greater.")