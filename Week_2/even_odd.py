def even_odd(n):
    return n % 2 == 0;

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print("Even") if even_odd(n) else print("Odd")