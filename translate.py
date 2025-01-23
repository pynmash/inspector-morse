import MorseCodePy as mpc


def to_morse(input, language="english"):
    morse_string = mpc.encode(input, language=language)
    return morse_string
