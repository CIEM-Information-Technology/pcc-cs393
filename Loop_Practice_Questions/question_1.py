# no more pennies
PENNIES_PER_NICKEL = 5
NICKEL = 0.05
total = 0.00

line = input("Enter the price of the item (blank to quit): ")

while line != "":
    total = total + float(line)
    line = input("Enter the price of the item (blank to quit): ")

print("The exact amount payable is %.02f" % total)
rounding_indicator = total * 100 % PENNIES_PER_NICKEL

if rounding_indicator < PENNIES_PER_NICKEL / 2:
    cash_total = total - rounding_indicator / 100
else:
    cash_total = total + NICKEL - rounding_indicator / 100
    
print("The cash amount payable is %.02f" % cash_total)