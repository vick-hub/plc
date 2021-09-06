import os
import sys
import random


def main():
    l1 = random.sample(range(0, 100), 100)
    l2 = random.sample(range(0, 100), 100)
    print(l1)
    print(l2)
    new_l = []
    i = 0
    j = 0
    while i <= len(l1)-1 and j <= len(l2)-1:
        t = l1[i] + l2[j]
        new_l.append(t)
        i += 1
        j += 1
    print(f"Pairwise sums: {new_l}")

    new_l = []
    i = 0
    j = 0
    while i <= len(l1)-1 and j <= len(l2)-1:
        t = l1[i] * l2[j]
        new_l.append(t)
        i += 1
        j += 1
    print(f"Cumulative pairwise product: {new_l}")
    print(f"Cum_prod sum: {sum(new_l)}")

    new_l1 = []
    new_l2 = []
    i = 0
    j = 0
    # fixme: no need for 'and' since l1 and l2 have the same length
    while i <= len(l1)-1 and j <= len(l2)-1:
        if i % 2 == 0 and j % 2 == 0:
            t = l1[i] + l2[j]
        new_l1.append(t)
        i += 1
        j += 1
    print(new_l1)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
