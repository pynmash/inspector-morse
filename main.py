from translate import to_morse, from_morse

if __name__ == "__main__":
    mode = input('Encode, or Decode? ')
    if mode.lower() == 'encode':
        input = input("Enter phrase to translate: ")
        print(to_morse(input))
    elif mode.lower() == 'decode':
        morse = input('Enter morse code: ')
        print(from_morse(morse))

