import os
import sys
import random


def main():
    m = list(range(50, 75))
    x = random.choices(m, weights=[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k=100)
    y = sorted(x)
    print(f" y = {y}")
    print(f" minimum is equal to first value: min = {min(y)}")
    print(f" maximum is equal to last value: max = {max(y)}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
