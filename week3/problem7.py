import os
import sys


def main():
    x = int(input("x: "))
    try:
        y = (x ** 3 - 9 * x) / (x ** 2 - 2 * x + 1)
        print(f" y = {y}")
    except ZeroDivisionError as err:
        print(f" Handling run-time error: {err}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
