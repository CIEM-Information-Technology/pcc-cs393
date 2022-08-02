from bonus_1 import howManyDaysInMonth


def isMagicDate(day, month, year):
    if day * month == year:
        return True
    else:
        return False


if __name__ == '__main__':
    for year in range(1901, 2001):
        print(f"Year {year}")
        print("-------------------")
        for month in range(1, 13):
            for day in range(1, howManyDaysInMonth(month, year) + 1):
                if isMagicDate(day, month, int(str(year)[2:])):
                    print(f"{day}-{month}-{year}")
        print("")
