def pascal(frac_1, frac_2):
    a, b = frac_1.split("/")
    c, d = frac_2.split("/")

    a = int(a) * int(d)
    c = int(c) * int(b)

    print("Pascal's principal proven") if a == c else print("Not proven")

if __name__ == "__main__":
    frac_1 = input("Input first fraction: ")
    frac_2 = input("Input second fraction: ")

    pascal(frac_1, frac_2)

