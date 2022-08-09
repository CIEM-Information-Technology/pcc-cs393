from bonus_1 import leapYear
from bonus_4 import ordinalDate


def gregorianDate(day: int, year: int):
    days_normal = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    month = 0
    d = day
    day_of_month = 0
    if leapYear(year):
        while True:
            d -= days_leap[month]
            if d == 0:
                day_of_month = days_leap[month]
                break
            elif d < 0:
                day_of_month = days_leap[month] - abs(d)
                month += 1
                break
            else:
                month += 1
    else:
        while True:
            d -= days_normal[month]
            if d == 0:
                day_of_month = days_normal[month]
                month += 1
                break
            elif d < 0:
                day_of_month = days_normal[month] - abs(d)
                month += 1
                break
            else:
                month += 1
    return f"{day_of_month}-{month}-{year}"


if __name__ == '__main__':
    days = int(input("Enter the number of days: "))
    date = input("Enter a date: ")
    day, month, year = [int(i) for i in date.split()]

    ordinal_days = ordinalDate(day, month, year)
    days = days + ordinal_days

    compare_days = 366 if leapYear(int(year)) else 365
    if days > compare_days:
        days = days - compare_days
        year = year + 1
        print(gregorianDate(days, year))
    else:
        print(gregorianDate(days, year))
