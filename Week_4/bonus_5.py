from bonus_1 import leapYear


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

# # TODO: implement the function in main
