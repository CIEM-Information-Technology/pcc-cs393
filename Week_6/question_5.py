def character_counts(s):
    counts = {}
    for ch in s:
        if ch in counts:
            counts[ch] = counts[ch] + 1
        else:
            counts[ch] = 1
    # Return the result
    return counts


if __name__ == '__main__':
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    counts1 = character_counts(s1)
    counts2 = character_counts(s2)

    if counts1 == counts2:
        print("Those strings are anagrams.")
    else:
        print("Those strings are not anagrams.")