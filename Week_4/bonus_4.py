from bonus_1 import leapYear


def ordinalDate(day: int, month: int, year: int):
    days_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = day

    if leapYear(year):
        for i in days_leap[:month-1]:
            result += i
        return result
    else:
        if day == 29 and month == 2:
            print("February does not have 29 days in this year.")
            print("Setting date as 1st March")
            result = 1
            month = 3

        for i in days_normal[:month-1]:
            result += i
        return result


if __name__ == '__main__':
    day, month, year = input("Enter day, month and year: ").split()
    print(f"Ordinal Date = {ordinalDate(int(day), int(month), int(year))}")
