import sys
import os
import random

def dummy():
    return 3

def main():
    # comparisons: ==, !=, <, <=, >, >=, is, is not
    x = 3
    y = 14
    print(x > y)
    print(x * y == 42)
    print(x * y != 2 * x + 3 * y)
    v = dummy()
    print(v is not None)
    # logical operators: and, or, not
    hat = 'red'
    car = 'blue'
    print(hat == 'red' and car == 'red')
    # and: True if all are True; False
    print(hat == 'red' or car != 'red')
    # or: at least one is True; False
    B = True
    print("B", B)
    print("not B", not B)
    print(not hat == 'red')
    # +=, -=
    v = 10
    print(f"v = {v}")
    # v = v + 1
    v += 1
    print(f"v = {v}")

    # v1 <= x <= v2
    # the random library
    X = random.random() # 0-1
    print(X)
    print(0 < X < 1) # print(X > 0 and X < 1)
    Y = random.randint(-10, 10)
    print(Y)
    print(-10 <= Y <= 10)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
