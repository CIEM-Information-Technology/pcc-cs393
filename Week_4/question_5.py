def calculateMedian(a, b, c):
    values = [int(a), int(b), int(c)]
    values.sort()
    return values[1]


if __name__ == '__main__':
    a, b, c = input("Enter three numbers: ").split()
    m = calculateMedian(a, b, c)
    print(f"The median is {m}.")
