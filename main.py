import MorseCodePy as mpc

input = input("Enter the English phrase you would linke to translate in to morse code:")

morse_string = mpc.encode(input, language="english")
print(morse_string)
