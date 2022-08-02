BASE_FARE = 4.00
EXTRA_FARE = 0.25


def calculateFare(distance_travelled):
    return BASE_FARE + ((distance_travelled * 1000) / 140) * EXTRA_FARE


if __name__ == '__main__':
    distance = float(input("Enter the distance distance_travelled: "))
    total_fare = calculateFare(distance)
    print("The total fare is ${:.2f}".format(total_fare))
