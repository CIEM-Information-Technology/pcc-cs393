def evenOdd(n: int):
  return True if n % 2 == 0 else False

n = int(input("Enter a number: "))
print("Even") if evenOdd(n) else print("Odd")