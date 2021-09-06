import os
import sys
import random


def main():
    l1 = random.sample(range(0, 100), 100)
    print(l1)
    new_l1 = []
    i = 0
    c = 0
    while i <= len(l1)-1:
        c += l1[i]
        new_l1.append(c)
    #    print(new_l1)
        i = i + 1
    print(f"Cumulative sum pairs: {new_l1}")

    new_l2 = []
    j = 0
    while j <= len(l1)-2:
        t = l1[j] + l1[j + 1]
        new_l2.append(t)
        j += 1
    print(f"Sum adjoining pairs: {new_l2}")

    new_l3 = []
    j = 0
    t = 2
    k = 4
    while j <= len(l1)-5:
        n = l1[j] + l1[t] + l1[k]
        j += 1
        t += 1
        k += 1
        new_l3.append(n)
    print(f"Sum of 3 alternate values: {new_l3}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
