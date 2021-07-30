import os
import sys
import random
import datetime
import glob


x = datetime.datetime.now()
dict1 = {"A": random.randint(0, 50), "B": random.randint(0, 50), "C": random.randint(0, 50)}
path = 'stock3'
try:
    os.makedirs(path)  # creating stock folder
except OSError as er:
    print(er)
file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file
list1 = []
set1 = set()
dict2 = {}
dict3 = {}


def stock():
    with open(file1, 'w') as f:
        for key, value in dict1.items():
            f.write('%s %d\n' % (key, value))


def stock_level():
    files = glob.glob('stock3/*.txt')  # help us to analyze multiple files
#    for dirName, fileList in os.walk('stock2'):
    for file in files:
        with open(file, 'r') as f:
            lines = f.readlines()
            for line in lines:
                list1.append(line.split())
        dict2.update(list1)
        for key, value in dict2.items():
            if key in dict3:
                dict3[key] += int(value)
            else:
                dict3[key] = int(value)
    for key, value in dict3.items():
        print(key, value)


def main():
    stock()
    stock_level()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
