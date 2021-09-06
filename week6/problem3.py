import os
import sys


def string_reverse(s):
    # todo: add a docstring
    string_reversed = []
    length = len(s)
    while length > 0:
        string_reversed += s[length - 1]
        length = length - 1
    return string_reversed


def main():
    s = input("Enter string: ")
    print(''.join(string_reverse(s))) # very good!
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
