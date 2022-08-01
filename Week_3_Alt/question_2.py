age_list = []

print("Enter the ages: (Enter a blank line to stop) ")
while True:
    age = input(":-> ")
    if len(age) == 0:
        print("End of input.")
        break
    else:
        age_list.append(int(age))

total_cost = 0.0
for age in age_list:
    if age <= 2:
        total_cost += 0.0
    if 3 <= age <= 12:
        total_cost += 14.0
    if age >= 65:
        total_cost += 18.0
    else:
        total_cost += 23.0

print("Total cost = ${:.2f}".format(total_cost))