import sys
from ft_filter import ft_filter


def filterString(S: str, N: int):
    """ Filter Strings """
    return list(ft_filter(lambda word: len(word) > N, S.split()))


def main():
    """ Main Function """
    number_of_args = len(sys.argv)
    N = 0
    S = ""
    if number_of_args == 3:
        try:
            S = str(sys.argv[1])
            N = int(sys.argv[2])
            results = filterString(S, N)
            print(results)
        except ValueError:
            print("AssertionError: the arguments are bad")
    else:
        print("AssertionError: the arguments are bad")


if __name__ == "__main__":
    main()
