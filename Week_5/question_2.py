def removeOutliers(data, num_outliers):
    retval = sorted(data)
    
    for _ in range(num_outliers):
        retval.pop()

    for _ in range(num_outliers):
        retval.pop(0)

    return retval


if __name__ == '__main__':
    x = int(input("How many items do you want to input? "))
    num_outliners = int(input("How many items do you want to remove? "))
    data = []
    for i in range(x):
        data.append(int(input()))

    new_data = removeOutliers(data, num_outliners)
    print(new_data)


