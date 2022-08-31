def remove_outliers(data_list, num):
    """
    removes the outliers from a list of data
    :param data_list: list of numerical data
    :param num: num of outliers to remove
    :return: list of new data
    """
    retval = sorted(data_list)
    retval = retval[num:-num]

    return retval


if __name__ == '__main__':
    x = int(input("How many items do you want to input? "))
    num_outliers = int(input("How many items do you want to remove? "))
    data = []
    for i in range(x):
        data.append(int(input()))

    new_data = remove_outliers(data, num_outliers)
    print(new_data)


