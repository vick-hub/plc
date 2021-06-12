import os
import sys
import random


def main():
    # 1. creating sets
    # set()
    s = set()
    print(s, type(s))
    s1 = {}
    print(s1, type(s))
    s2 = {1, 2, 3}
    print(s2)
    s3 = set([1, 2, 3, 4])
    print(f"s3 = {s3}")
    # print(s3[0])
    # frozenset()
    f1 = frozenset()
    print(f1, type(f1))

    # 2. modifying sets
    # set.add(elem)
    s3.add(27)
    print(s3)
    for i in random.choices(range(10, 20), k=10):
        s3.add(i)
        print(i)
    print(s3)
    # set.remove(elem)
    s3.remove(27)
    print(s3)
    # s3.remove(99)  # KeyError
    # set.discard(elem)
    s3.discard(99)  # Avoid KeyError

    # 3. membership (in, not in)

    # 4. castings on sets
    # len(s)
    list_s3 = list(s3)
    print(list_s3, type(list_s3))
    # list(s), tuple(s)

    # 5. methods/operations
    s1 = set(random.choices(range(100, 115), k=15))
    s2 = set(random.choices(list(s1), k=10))
    print(f"s1 = {s1}, {len(s1)}")
    print(f"s2 = {s2}, {len(s2)}")
    # <=, <, set.issubset(other)
    print(f"s2 is a subset of s1: {s2 <= s1}")  # subset
    print(f"s2 is a proper subset of s1: {s2 < s1}")  # proper subset
    # >=, >, set.issuperset(other)
    print(f"s1 is a proper superset of s2: {s1 > s2}")
    s5 = set(random.choices(range(100, 115), k=15))
    s6 = set(random.choices(range(100, 115), k=15))
    print(f"s5 = {s5}, {len(s5)}")
    print(f"s6 = {s6}, {len(s6)}")
    # |, set.union(*others)
    s7 = s5.union(s6) # combined
    print(f"union = {s7}, {len(s7)}")
    print(s5 | s6)
    # &, set.intersection(*others)
    s8 = s5.intersection(s6)
    print(f"intersect = {s8}, {len(s8)}") # occurs in both
    # -, set.difference(*others)
    s9 = s5.difference(s6)
    s10 = s6.difference(s5)
    print(s5)
    print(s6)
    print(f"difference = {s9}, {len(s9)}")
    print(f"difference = {s10}, {len(s10)}")

    f = frozenset([1, 2, 3, 4, 5])
    f1 = frozenset(range(10, 15))
    # f.add(10)
    print(f"frozenset = {f}")
    print(f"frozenset = {f1}")
    f2 = f | f1
    print(f"union: {f2}")
    # ^, set.symmetric_difference(other)
    # set.copy()
    # set.pop()
    # set.clear()
    # ==
    # |=, set.update(*others)
    # &=, set.intersection_update(*others)
    # -=, set.difference_update(*others)
    # ^=, set.symmetric_difference_update(other)

    # test your grasp on the fundamentals: https://bit.ly/3xlpwnz
    # feedback: https://bit.ly/3pLm9U9
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
