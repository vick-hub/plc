import os
import sys
import random
import string


# """To make a DNA string with a random composition of the letters we can first make a list of
# random letters and then join all those letters to a string:"""
def main():
    alphabet = list('ACGT')
    dna = [random.choice(alphabet) for i in range(100)]
    dna = ''.join(dna)  # join the list elements to a string
    print(dna)

    l1 = []
    r = 0
    s = 3
    for i in range(len(dna)-2):
        t = dna[r:s]
        r += 1
        s += 1
        l1.append(t)
    # print(l1)
    dt = dict()
    for ele in l1:
        if ele not in dt:
            dt[ele] = 1
        else:
            dt[ele] = dt[ele] + 1
    # print(dt)
    print('k = 3')
    print("3-mer count")
    print('-' * 50)
    for keys, values in dt.items():
        print(keys, " ", values)
    print('=' * 50)

    l1 = []
    r = 0
    s = 4
    for i in range(len(dna)-3):
        t = dna[r:s]
        r += 1
        s += 1
        l1.append(t)
    # print(l1)
    dt = dict()
    for ele in l1:
        if ele not in dt:
            dt[ele] = 1
        else:
            dt[ele] = dt[ele] + 1
    # print(dt)
    print('k = 4')
    print("4-mer count")
    print('-' * 50)
    for keys, values in dt.items():
        print(keys, " ", values)
    print('=' * 50)

    l1 = []
    r = 0
    s = 5
    for i in range(len(dna)-4):
        t = dna[r:s]
        r += 1
        s += 1
        l1.append(t)
    # print(l1)
    dt = dict()
    for ele in l1:
        if ele not in dt:
            dt[ele] = 1
        else:
            dt[ele] = dt[ele] + 1
    # print(dt)
    print('k = 5')
    print("5-mer count")
    print('-' * 50)
    for keys, values in dt.items():
        print(keys, " ", values)
    print('=' * 50)

    l1 = []
    r = 0
    s = 6
    for i in range(len(dna)-5):
        t = dna[r:s]
        r += 1
        s += 1
        l1.append(t)
    # print(l1)
    dt = dict()
    for ele in l1:
        if ele not in dt:
            dt[ele] = 1
        else:
            dt[ele] = dt[ele] + 1
    # print(dt)
    print('k = 6')
    print("6-mer count")
    print('-' * 50)
    for keys, values in dt.items():
        print(keys, " ", values)
    print('=' * 50)

    l1 = []
    r = 0
    s = 7
    for i in range(len(dna)-6):
        t = dna[r:s]
        r += 1
        s += 1
        l1.append(t)
    # print(l1)
    dt = dict()
    for ele in l1:
        if ele not in dt:
            dt[ele] = 1
        else:
            dt[ele] = dt[ele] + 1
    # print(dt)
    print('k = 7')
    print("7-mer count")
    print('-' * 50)
    for keys, values in dt.items():
        print(keys, " ", values)
    print('=' * 50)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
