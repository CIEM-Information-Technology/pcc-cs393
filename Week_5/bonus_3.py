from bonus_2 import token_list


def identify_unary(tokens):
    """
    Identify the unary operators from a list of tokens
    :param tokens: list of tokens
    :return: a modified list with idenfied unary operators
    """
    retval = []

    for i in range(len(tokens)):
        if i == 0 and (tokens[i] == "+" or tokens[i] == "-"):
            retval.append("u" + tokens[i])
        elif i > 0 and (tokens[i] == "+" or tokens[i] == "-") and \
             (tokens[i - 1] == "+" or tokens[i - 1] == "-" or
              tokens[i - 1] == "*" or tokens[i - 1] == "/" or
              tokens[i - 1] == "("):
            retval.append("u" + tokens[i])
        else:
            retval.append(tokens[i])

    return retval


if __name__ == '__main__':
    exp = input("Enter a mathematical expression: ")
    tokens = token_list(exp)
    print("The tokens are:", tokens)

    marked = identify_unary(tokens)
    print("With unary operators marked: ", marked)
