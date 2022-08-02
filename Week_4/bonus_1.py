def leapYear(year: int) -> bool:
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def howManyDaysInMonth(month: int, year: int):
    normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return leap[month - 1] if leapYear(year) else normal[month - 1]


if __name__ == '__main__':
    month = int(input("Enter a month [1-12]: "))
    year = int(input("Enter a year: "))
    print(f"Days in month = {howManyDaysInMonth(month, year)}")
