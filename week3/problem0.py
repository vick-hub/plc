import os
import sys


def main():
    t = int(input("t: "))
    s = int(input("S: "))
    y = list(range(t, s))
    print(f" y = {y}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
