import os
import sys


def list1():
    # fixme: do not use max() and min()
    list2 = [100, 150, 200, 20, 35, 95, 79]
    print(f"Maximum: {max(list2)}")
    print(f"Minimum: {min(list2)}")


def main():
    list1()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
