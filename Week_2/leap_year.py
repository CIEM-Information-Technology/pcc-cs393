def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


if __name__ == '__main__':
    year = int(input("Enter a year: "))

    print(f"{year} is a leap year") if leap_year(year) else print(f"{year} is not a leap year")
    
