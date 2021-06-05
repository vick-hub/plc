import os
import sys


def main():
    # create
    t = tuple()
    print(t, type(t))
    print(len(t))
    s = ()
    print(s, type(s))
    s = ('car')
    print(s, type(s))
    i = (0)
    print(i, type(i))
    t = (0,)
    print(t, type(t))
    u = 5, 6
    print(u, type(u))
    # immutability: cannot be changed once created
    t = (5, 6, 7, 8, 9, 10)
    print(f"t[0] = {t[0]}")
    print(f"t[1:3] = {t[1:3]}")
    # t[3] = 12 TypeError
    # del t[3] TypeError
    # 'modifying' tuples
    t = (6,) * 12
    print(t)
    u = 1, 3
    v = 7, 12
    print(u, v)
    w = u + v
    print(w)
    # string are immutable
    s = "Today is a good day."
    # s[8] = 'y' TypeError
    # casting of containers
    l = list(range(5, 120, 4))
    print(l, type(l))
    t = tuple(l)
    print(t, type(t))
    l2 = list(t)
    print(l2)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
