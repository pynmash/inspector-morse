import MorseCodePy as mpc


def to_morse(input, language="english"):
    morse_string = mpc.encode(input, language=language)
    return morse_string

def from_morse(morse, language='english'):
    decoded_string = mpc.decode(morse, language)
    return decoded_string
