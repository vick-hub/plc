import os
import sys
import random


def main():
    l1 = random.sample(range(0, 100), 100)
    l2 = random.sample(range(0, 100), 100)
    print(l1)
    print(l2)
    l3 = []
    for t, k in zip(l1, l2):
        s = t + k
        l3.append(s)
    print(f" Pairwise sums: {l3}")
    l4 = []
    for t, k in zip(l1, l2):
        s = t * k
        l4.append(s)
    print(l4)
    print(f"cum_prod: {sum(l4)}")

    l5 = []
    # fixme: this is only evens; you need to include odds
    for t, k in zip(l1, l2):
        if t % 2 == 0 and k % 2 == 0:
            r = t + k
            l5.append(r)
    print(l5)
    print(f" Sum of even pairs: {sum(l5)}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
