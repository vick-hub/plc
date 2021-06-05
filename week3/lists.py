import os
import sys


def main():
    # creating lists
    l = list()
    print(l, type(l))
    print(f"the length of the list is {len(l)}")
    l1 = [5, 6, 7, 8]
    print(f"the length of l1 is {len(l1)}: {l1}")
    print(dir(l1))
    # dir() show attributes on object
    # membership: in, not in
    print(6 in l1)
    print(12 not in l1)
    print(not 12 in l1)
    # + operator on lists
    A = list()
    B = A + [7, 8, 9]
    print(f"A = {A}")
    print(f"B = {B}")
    print(id(A))
    print(id(B))
    u = [12, 13, 14, 15]
    print(f"u = {u}")
    v = u.copy() # use copy to make a copy; don't use assignment
    print(f"v = {v}")
    v += [97, 98]
    print(f"u = {u}, v = {v}")
    print(f"id of u = {id(u)}")
    print(f"id of v = {id(v)}")
    # * on lists
    D = [3] * 20
    print(f"D = {D} of length {len(D)}")
    # TypeError
    # E = [3] * [4]
    # print(E)
    # lengths, min, max
    F = 20 * [3] # commutative
    print(F)
    print(f"minimun value: {min(v)}")
    print(f"maximum value: {max(v)}")
    print(f"v = {v}")
    print(f"the first item is {v[0]}")
    print(f"the second item is {v[1]}")
    print(f"the last item is {v[-1]}")
    print(f"the last but one item is {v[-2]}")
    # IndexError: accessing out of bounds
    # print(f"the 6th is {v[6]}")
    # print(f"the -7th is {v[-7]}")
    # .index()
    print(f"12 is at {v.index(12)}")
    # ValueError
    # print(v.index(100))
    # .count()
    v = [3] * 10 + [5, 6, 7, 8]
    print(v)
    print(f"There are {v.count(3)} instances of 3 in v")
    # also apply to string objects!!!
    print("-" * 100)
    s = "This is a good sentence to work with."
    print(s[12])
    # slices
    print(v[3:7])
    print(v[3:7:2]) # list[start:stop:step]
    r = list(range(20)) # 0-19
    print(r)
    print(r[3:10])
    print(r[3:10:2]) # 3, 5, 7, 9
    w = list(range(15, 20)) # 15, 16, 17, 18, 19
    print(w)
    x = list(range(15, 20, 2)) # 15, 17, 19
    print(x)
    k = list(range(12, 100, 3))
    print(f"k = {k}")
    print(k[-10:-1])
    print(k[-10:-1:2])
    print(k[-1:-10:-2])
    # default
    print(k[::])
    print(k[::2])
    print(k[:12])
    # replace using index
    k[12] = 1000
    print(f"new k = {k}")
    k[14:18] = [77] * 4
    print(k)
    # del
    print(len(k))
    del k[17]
    print(len(k))
    print(k)
    # .append()
    K = list()
    K.append(6)
    print(K)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
