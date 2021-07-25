import os
import sys
import random
import datetime


def main():
    dict1 = {"A": random.randint(0, 50), "B": random.randint(0, 50), "C": random.randint(0, 50)}
    dict2 = {}
    x = datetime.datetime.now()

    path = 'stock'
    try:
        os.makedirs(path)  # creating stock folder
    except OSError as er:
        print(er)
    file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file
    with open(file1, 'w') as f:
        for key, value in dict1.items():
            f.write('%s %s\n' % (key, value))

    path = 'product'
    try:
        os.makedirs(path)  # creating product folder
    except OSError as er:
        print(er)
    file2 = os.path.join(path, str(x) + '.txt')  # creating timestamp file
    with open(file1, 'r') as fr:
        data = fr.readlines()
        with open(file2, 'w') as fw:
            for line in data:
                values = line.split()
#                dict2['M'] = values[1]
#                dict2['N'] = values[2]
#                for key, value in dict2.items():
#                    fw.write('%s %s\n' % (key, value))

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())