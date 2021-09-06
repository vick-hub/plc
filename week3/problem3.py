import os
import sys
import random


def main():
    m = list(range(0, 4))
    x = random.choices(m, weights=[1, 1, 1, 1], k=10)
    print(f" 0 = {x.count(0)}")
    print(f" 1 = {x.count(1)}")
    print(f" 2 = {x.count(2)}")
    print(f" 3 = {x.count(3)}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
