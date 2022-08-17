# compute the perimeter of a polygon from co-ordinates
from math import sqrt

perimeter = 0

first_x = float(input("Enter the first x-coordinate: "))
first_y = float(input("Enter the first y-coordinate: "))

prev_x = first_x
prev_y = first_y

line = input("Enter the next x-coordinate (blank to quit): ")

while line != "":
    x = float(line)
    y = float(input("Enter the next y-coordinate: "))
    dist = sqrt((prev_x - x) ** 2 + (prev_y - y) ** 2)
    perimeter = perimeter + dist
    prev_x = x
    prev_y = y
    line = input("Enter the next x-coordinate (blank to quit): ")

dist = sqrt((first_x - x) ** 2 + (first_y - y) ** 2)
perimeter = perimeter + dist
print("The perimeter of that polygon is", perimeter)
