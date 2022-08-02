def checkTriangle(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return False
    elif a + b < c or b + c < a or a + c < b:
        return False
    else:
        return True


if __name__ == '__main__':
    a, b, c = input("Enter three sides: ").split()
    if checkTriangle(int(a), int(b), int(c)):
        print("Can form a triangle.")
    else:
        print("Can't form a triangle.")
