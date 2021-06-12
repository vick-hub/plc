import os
import sys


def main():
    # 1. creating sets
    # set()
    # frozenset()

    # 2. modifying sets
    # set.add(elem)
    # set.remove(elem)
    # set.discard(elem)

    # 3. membership (in, not in)

    # 4. castings on sets
    # len(s)
    # list(s), tuple(s)

    # 5. methods/operations
    # <=, <, set.issubset(other)
    # >=, >, set.issuperset(other)
    # |, set.union(*others)
    # &, set.intersection(*others)
    # -, set.difference(*others)
    # ^, set.symmetric_difference(other)
    # set.copy()
    # set.pop()
    # set.clear()
    # ==
    # |=, set.update(*others)
    # &=, set.intersection_update(*others)
    # -=, set.difference_update(*others)
    # ^=, set.symmetric_difference_update(other)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
