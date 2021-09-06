import os
import sys


# fixme: can you think of a better name in line with what this function does?
def palindrome(word):
    # todo: add a docstring; read the class notes
    return word == word[::-1]


def main():
    word = input("word: ")
    answer = palindrome(word)
    if answer:
        print('yes')
    else:
        print('no')
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
