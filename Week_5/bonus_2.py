def token_list(s):
    """
    Converts a mathematical expression into a list of tokens
    :param s: the string to tokenize
    :return: a list of the tokens in s or an empty list
    """
    # remove all the whitespaces
    s = s.replace(" ", "")
    pre_defined_tokens = ["+", "-", "*", "/", "^", "(", ")"]
    tokens = []
    i = 0
    while i < len(s):
        # handle the toknes
        if s[i] in pre_defined_tokens:
            tokens.append(s[i])
            i += 1
        # handle a number without a leading + or -
        elif "0" <= s[i] <= "9":
            num = ""
            # keep on adding characters as long as they are digits
            while i < len(s) and "0" <= s[i] <= "9":
                num += s[i]
                i += 1
            tokens.append(num)
        else:
            return []
    return tokens


if __name__ == '__main__':
    exp = input("Enter a mathematical expression: ")
    tkn = token_list(exp)
    print("The tokens are: ")
    print(tkn)

