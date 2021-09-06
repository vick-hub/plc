import os
import sys


def main():
    one = set(range(2, 100, 1))
    print(one)
    two = set(range(4, 100, 2))
    print(two)
    three = set(range(6, 100, 3))
    print(three)
    five = set(range(10, 100, 5))
    print(five)
    seven = set(range(14, 100, 7))
    print(seven)
    d1 = one.difference(two)
    d2 = d1.difference(three)
    d3 = d2.difference(five)
    d4 = d3.difference(seven)
    print(sorted(d4)) # very good!
    # They are all prime numbers
    # By changing 100 to 1000
    # prove it!
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
