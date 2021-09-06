import os
import sys


def main():
    # fixme: choose meaningful names for variables; 'sent' is confusing; don't be lazy! ;-)
    sent = input("Enter a sentence: ").split(" ")
    s = []
    # fixme: too complex!
    s2 = dict()
    for i in sent:
        s.append(i)
    # print(s)
    s1 = enumerate(s)
#     print(s1)
    for i in s1:
        if i is not s2:
            s2[i] = 1
        else:
            s2[i] = s2[i] + 1
    for k, v in s2:
        print(k, '->', v)

    # ... or you can simply call enumerate on the for loop
    for i, w in enumerate(sent):
        print(f"{i} --> {w}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
