import sys


def main():
    """
    Program to encode alphanumeric strings into Morse code.
    """
    NESTED_MORSE = {" ": " / ",
                    "A": ".-",
                    "B": "-...",
                    "C": "-.-.",
                    "D": "-..",
                    "E": ".",
                    "F": "..-.",
                    "G": "--.",
                    "H": "....",
                    "I": "..",
                    "J": ".---",
                    "K": "-.-",
                    "L": ".-..",
                    "M": "--",
                    "N": "-.",
                    "O": "---",
                    "P": ".--.",
                    "Q": "--.-",
                    "R": ".-.",
                    "S": "...",
                    "T": "-",
                    "U": "..-",
                    "V": "...-",
                    "W": ".--",
                    "X": "-..-",
                    "Y": "-.--",
                    "Z": "--..",
                    "0": "-----",
                    "1": ".----",
                    "2": "..---",
                    "3": "...--",
                    "4": "....-",
                    "5": ".....",
                    "6": "-....",
                    "7": "--...",
                    "8": "---..",
                    "9": "----."}
    try:
        assert len(sys.argv) - 1 == 1, "the arguments are bad"
        # check if all characters in the string are alphanumeric or a space
        assert sys.argv[1].replace(" ", "").isalnum(), "the arguments are bad"
        # make all characters uppercase
        string = sys.argv[1].upper()
        # list comprehension to get the morse code for each character
        morse_code = [NESTED_MORSE[char] for char in string]
        # join the morse code list into a string
        print("".join(morse_code))
    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
