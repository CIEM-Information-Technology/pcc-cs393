problem = input("Enter the math problem : ").split()
x = float(problem[0])
y = problem[1]
z = float(problem[2])
if y == '+':
  r = x + z
  print("{:.1f}".format(r))
elif y == '-':
  r = x - z
  print("{:.1f}".format(r))
elif y == '*':
  r = x * z
  print("{:.1f}".format(r))
elif y == '/':
  if z != 0:
    r = x - z
    print("{:.1f}".format(r))
  else:
    print("Can't divide by zero")
else:
  print("Not a valid input")