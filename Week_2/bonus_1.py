answer = input("What is the answer to the life, universe, and everything? ")
answer = answer.lower()

if answer in ['42', 'forty-two', 'forty two']:
  print("Yes")
else:
  print("No")