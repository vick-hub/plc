import os
import sys
import random
import string


def main():
    values = random.choices(range(100), k=10)
    keys = random.choices(string.ascii_lowercase, k=10)
    values1 = random.choices(range(100), k=10)
    keys1 = random.choices(string.ascii_lowercase, k=10)
    d1 = dict(zip(keys, values))
    d2 = dict(zip(keys1, values1))
    # print(d1)
    # print(d2)
    d3 = dict(d1)
    d3.update(d2)
    for i, j in d1.items():
        for x, y in d2.items():
            if i == x:
                d3[i] = (j+y)
    print(d3)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
