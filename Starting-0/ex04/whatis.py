import sys

number_of_args = len(sys.argv)

if number_of_args > 2:
    print("AssertionError: more than one argument is provided")
elif number_of_args == 2:
    arg = sys.argv[1]
    try:
        int_value = int(arg)
        if int_value % 2 == 0:
            print("I'am Even")
        else:
            print("I'am Odd")
    except ValueError:
        print("AssertionError: argument is not an integer")


## This is to iterate through arguments
# for arg in sys.argv:
#     print(arg)

## This is to print the number of arguments
# print(len(sys.argv))