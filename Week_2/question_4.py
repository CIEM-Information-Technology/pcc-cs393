def leapYear(year: int):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

y = int(input("Enter a year: "))
print("Leap year.") if leapYear(y) else print("Not leap year.")