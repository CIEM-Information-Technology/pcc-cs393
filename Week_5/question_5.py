if __name__ == '__main__':
    numbers = []
    print("Enter numbers (blank to exit): ")
    while True:
        n = input()
        if n == "":
            break
        numbers.append(int(n))
    numbers = sorted(numbers)
    for i in numbers:
        print(i)

