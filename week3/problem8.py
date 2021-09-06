import os
import sys
import random


def main():
    x = random.sample(range(0, 9), 5)
    y = int(input("y: "))
    try:
        assert 0 <= y <= 9
        print(f"Check if y is not in x: = {y not in x}")
    except AssertionError:
        print(f"error: invalid entry {y} should between 0 <= y <= 9")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
