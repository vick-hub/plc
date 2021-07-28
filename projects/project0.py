import os
import sys
import random
import datetime


x = datetime.datetime.now()
dict1 = {"A": random.randint(0, 50), "B": random.randint(0, 50), "C": random.randint(0, 50)}
path = 'stock'
try:
    os.makedirs(path)  # creating stock folder
except OSError as er:
    print(er)
file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file


def stock():
    with open(file1, 'w') as f:
        for key, value in dict1.items():
            print(key, value, file=f)


list1 = []
list2 = []
dict2 = {}

path1 = 'product'
try:
    os.makedirs(path1)  # creating product folder
except OSError as er:
    print(er)
file2 = os.path.join(path1, str(x) + '.txt')  # creating timestamp file


def product():
    with open(file1, 'r') as fr:
        with open(file2, 'w') as fw:
            lines = fr.readlines()
            for line in lines:
                list1.append(line.split())
            x = int(list1[0][1]) // 2
            y = int(list1[1][1]) // 3
            z = int(list1[2][1]) // 4
            m = x + y + z
            n = int(list1[0][1]) + z
            dict2['M'] = m
            dict2['N'] = n
            for k, v in dict2.items():
                print(k, v, file=fw)


def stock_level():
    with open(file1, 'r') as fr:
        lines = fr.readlines()
        for line in lines:
            list1.append(line.split())
        x = int(list1[0][1])
        x += x
        y = int(list1[1][1])
        y += y
        z = int(list1[2][1])
        z += z
        print(f"A {x}")
        print(f"B {y}")
        print(f"C {z}")


def product_level():
    with open(file2, 'r') as fw:
        lines = fw.readlines()
        for line in lines:
            list2.append(line.split())
        x = int(list2[0][1])
        x += x
        y = int(list2[1][1])
        y += y
        print(f"M {x}")
        print(f"N {y}")


def main():
    stock()
    product()
    print('stock level: ')
    stock_level()
    print('product level: ')
    product_level()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
