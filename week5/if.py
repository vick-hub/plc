import os
import sys


def main():
    # simple if
    x = int(input("x: "))
    print(f"x > 10: {x > 10}")
    if x > 10:
        print("x > 10")

    # if/else
    x = int(input("x: "))
    if x > 10:
        print("x > 10")
    else:  # assignment expression evaluates to False
        print("x <= 10")

    # if/elif/else
    x = int(input("x: "))
    if x > 10:
        print("x > 10")
    elif x < 10:  # elif cannot be at the beginning; must come after an 'if'
        print("x < 10")
    else:  # only one other case; x = 10
        print("x == 10")

    # exhaustiveness
    letter = input("pick a letter: ")
    if letter.lower() == 'a':
        print("a")
    elif letter.lower() == 'b':
        print("b")
    # include c-z
    else:
        print("I don't know what that is!")

    # key: ensure that your if/elif/else are exhaustive for your application
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
