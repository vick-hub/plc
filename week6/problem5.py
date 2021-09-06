import os
import sys


# fixme: think of a better name
def double(text, a=2):
    # todo: docstring
    # very good!
    return ''.join([x * a for x in text])


def main():
    a = 3
    text = input("enter a sentence: ")
    print(double(text, a))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
