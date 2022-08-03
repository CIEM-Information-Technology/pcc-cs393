TSP_PER_TBSP = 3
TSP_PER_CUP = 48


def reduceMeasure(num, unit):
    unit = unit.lower()
    if unit == "teaspoon" or unit == "teaspoons":
        teaspoons = num
    elif unit == "tablespoon" or unit == "tablespoons":
        teaspoons = num * TSP_PER_TBSP
    elif unit == "cup" or unit == "cups":
        teaspoons = num * TSP_PER_CUP

    cups = teaspoons // TSP_PER_CUP
    teaspoons = teaspoons - cups * TSP_PER_CUP
    tablespoons = teaspoons // TSP_PER_TBSP
    teaspoons = teaspoons - tablespoons * TSP_PER_TBSP

    result = ""

    if cups > 0:
        result = result + str(cups) + " cup"
        if cups > 1:
            result = result + "s"

    if tablespoons > 0:
        result = result + ", "
        result = result + str(tablespoons) + " tablespoon"
        if tablespoons > 1:
            result = result + "s"

    if teaspoons > 0:
        if result != "":
            result = result + ", "
            result = result + str(teaspoons) + " teaspoon"
            if teaspoons > 1:
                result = result + "s"

    if result == "":
        result = "0 teaspoons"

    return result
