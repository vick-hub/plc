import os
import sys
import random

"""
Notes:
- you have reverted to untidy code! ensure you have main() and 'if __name__ == "__main__": sys.exit(main())'
- stick to good practice!
"""


def main():
    l1 = random.sample(range(0, 100), 100) # good
    print(l1)
    new_l = []
    add = 0
    for number in l1:
        add += number
        new_l.append(add)
    print(f"Cumulative sum pairs: {new_l}")

    new_l1 = []
    for t in range(len(l1)-1):
        r = l1[t] + l1[t + 1]
        new_l1.append(r)
    print(f"Sum adjoining pairs: {new_l1}")

    new_l2 = []
    t = 2
    k = 4
    j = 0
    # very good
    for i in range(len(l1)-4):
        a = l1[j] + l1[t] + l1[k]
        t += 1
        k += 1
        j += 1
        new_l2.append(a)
    print(f"Sum of 3 alternate values: {new_l2}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
