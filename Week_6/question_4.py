s = input("Enter a string: ")

characters = {}
for ch in s:
    characters[ch] = True

print(f"That string contained {len(characters)} unique character(s).")
