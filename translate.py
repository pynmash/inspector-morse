import MorseCodePy as mpc


def to_morse(input: str , language: str = "english") -> str:
    """Convert a string from english to a string containing morse code.

    Keyword arguments:
    input -- The string to be converted.
    language -- The language the input is in (default = "english")
    """
    morse_string = mpc.encode(input, language=language)
    return morse_string

def from_morse(morse: str, language: str = 'english') -> str:
    """ Convert a morse code string in to the specified language.
    
    Keyword arguments:
    input -- The string to be converted.
    language -- The language the input is in (default = "english")
    """
    decoded_string = mpc.decode(morse, language)
    return decoded_string
