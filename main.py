from translate import to_morse, from_morse

if __name__ == "__main__":
    mode: str = input('Encode, or Decode? ')
    if mode.lower() == 'encode':
        input: str = input("Enter phrase to translate: ")
        print(to_morse(input, ))
    elif mode.lower() == 'decode':
        morse:str = input('Enter morse code: ')
        print(from_morse(morse))

