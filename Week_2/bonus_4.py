def convert(time):
  h, m = [float(i) for i in time.split(":")]
  m = m / 60
  return h + m

def main():
  time_string = input("Please enter time : (HH:MM) ")
  t = convert(time_string)

  if 7 <= t <= 8:
    print("Breakfast time.")
  elif 12 <= t <= 13:
    print("Lunch time")
  elif 18 <= t <= 19:
    print("Dinner time")

main()