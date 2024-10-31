import sys


NESTED_MORSE = {
    " ": "/",
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
    "9": "----."
}


def doMorse(string: str):
    """ Encode text into Morse """
    morse = " "
    text = [NESTED_MORSE[char.upper()] for char in string]
    return morse.join(text)


def main():
    """ Main Function """
    try:
        number_of_args = len(sys.argv)
        if number_of_args == 2:
            string = sys.argv[1]
            for c in string:
                if not c.isalpha() and not c.isdigit() and not c == " ":
                    raise ValueError("NG")
            print(doMorse(string))
        else:
            print("AssertionError: the arguments are bad")
    except ValueError:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
