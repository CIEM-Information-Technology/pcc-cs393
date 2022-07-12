def greater_num(a, b):
    print(f"{a} > {b}") if a > b else print(f"{b} > {a}")

if __name__ == "__main__":
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    greater_num(a, b)