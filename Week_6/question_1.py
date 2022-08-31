def reverse_lookup(data, value):
    keys = []
    for key in data:
        if data[key] == value:
            keys.append(key)
    return keys


if __name__ == '__main__':
    fr_en = {"le": "the", "la": "the", "livre": "book", "pomme": "apple"}
    print("The french words for ’the’ are: ", reverse_lookup(fr_en, "the"))
    print("Expected: [’le’, ’la’]")
    print()
    print("The french word for ’apple’ is: ", reverse_lookup(fr_en, "apple"))
    print("Expected: [’pomme’]")
    print()
    print("The french word for ’asdf’ is: ", reverse_lookup(fr_en, "asdf"))
    print("Expected: []")
