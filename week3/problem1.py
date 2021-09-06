import os
import sys
import random


def main():
    x = random.sample(range(0, 9), 5)
    y = int(input("y: "))
    print(f"Check if y is not in x: = {y not in x}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
