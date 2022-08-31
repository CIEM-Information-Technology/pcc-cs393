def morse_code_decoder(morse_code):
    code_book = {'.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E',
                 '..-.': 'F', '--.': 'G', '....': 'H', '..': 'I', '.---': 'J',
                 '-.-': 'K', '.-..': 'L', '--': 'M', '-.': 'N', '---': 'O',
                 '.--.': 'P', '--.-': 'Q', '.-.': 'R', '...': 'S', '-': 'T',
                 '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X', '-.--': 'Y',
                 '--..': 'Z', '.....': ' '}
    translation = ""
    # Morse code is separated by empty space chars
    morse_code = morse_code.split(' ')
    for x in morse_code:
        translation += code_book.get(x)

    return translation


if __name__ == '__main__':
    coded = input("Enter morse code: ")
    decoded = morse_code_decoder(coded)
    print(decoded)
