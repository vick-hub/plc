import os
import sys
import random
import datetime


def main():
    x = datetime.datetime.now()
    dict1 = {"A": random.randint(0, 50), "B": random.randint(0, 50), "C": random.randint(0, 50)}
    path = 'stock'
    try:
        os.makedirs(path)  # creating stock folder
    except OSError as er:
        print(er)
    file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file
    with open(file1, 'w') as f:
        for key, value in dict1.items():
            print(key, value, file=f)

    path = 'product'
    try:
        os.makedirs(path)  # creating product folder
    except OSError as er:
        print(er)
    file2 = os.path.join(path, str(x) + '.txt')  # creating timestamp file

    list1 = []
    dict2 = {}

    def consumption():
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
    consumption()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
