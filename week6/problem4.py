import os
import sys
import random


def doubling():
    # todo: docstring
    list2 = []
    for i in range(15):
        list1 = random.uniform(0, 100)
        list2.append(list1)
    print(list2)
    list_doubled = list(map(lambda x: x * 2, list2))
    print(list_doubled)


def main():
    # fixme: no need for a function
    doubling()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
