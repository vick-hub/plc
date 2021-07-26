import os
import sys
import random
import datetime

x = datetime.datetime.now()
dict1 = {"A": random.randint(0, 50), "B": random.randint(0, 50), "C": random.randint(0, 50)}
path = 'stock2'
try:
    os.makedirs(path)  # creating stock folder
except OSError as er:
    print(er)
file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file
with open(file1, 'w') as f:
    for key, value in dict1.items():
        print(key, value, file=f)

path = 'product1'
try:
    os.makedirs(path)  # creating product folder
except OSError as er:
    print(er)
file2 = os.path.join(path, str(x) + '.txt')  # creating timestamp file

list1 = []
with open(file1, 'r') as f:
    def consumption(x, y, z):
        lines = f.readlines()
        for line in lines:
            list1.append(line.split())
        a = (list1[0][1])
        b = list1[1][1]
        c = list1[2][1]
        return a, b, c


def main():
    consumption(2, 3, 4)

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
