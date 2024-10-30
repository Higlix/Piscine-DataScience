import sys


def countChars(sentence: str):
    character_count = len(sentence)
    upper_count = 0
    lower_count = 0
    punc_count = 0
    space_count = 0
    digit_count = 0
    p = ["!", ".", ",", "?", "-", "_", '"', "'", ";", ":", "{", "}", "[", "]"]
    for c in sentence:
        if c.islower():
            lower_count += 1
        elif c.isupper():
            upper_count += 1
        elif c.isdigit():
            digit_count += 1
        elif c.isspace():
            space_count += 1
        elif c in p:
            punc_count += 1
    print(f"The text contains {character_count} characters:")
    print(f"{upper_count} upper letters")
    print(f"{lower_count} lower letters")
    print(f"{punc_count} punctuation marks")
    print(f"{space_count} spaces")
    print(f"{digit_count} digits")


def takeInput() -> str:
    sentence = input("What is the text to count?\n")
    if len(sentence) > 0:
        return sentence
    return ""


def main():
    number_of_args = len(sys.argv)
    sentence = ""
    if number_of_args == 1:
        sentence = takeInput()
    elif number_of_args == 2:
        sentence = sys.argv[1]
    else:
        print("AssertionError: more than one argument is provided")
        return ""
    countChars(sentence)


if __name__ == "__main__":
    main()
