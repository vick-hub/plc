import os
import sys
import random
import datetime
import glob


x = datetime.datetime.now()
dict1 = {"A": random.randint(8, 50), "B": random.randint(8, 50), "C": random.randint(8, 50)}
path = 'stock'
try:
    os.makedirs(path)  # creating stock folder
except OSError as er:
    print(er)
file1 = os.path.join(path, str(x) + '.txt')  # creating timestamp file

path1 = 'product'
try:
    os.makedirs(path1)  # creating product folder
except OSError as er:
    print(er)
file2 = os.path.join(path1, str(x) + '.txt')  # creating timestamp file
files = glob.glob('stock/*.txt')  # glob help us to analyze multiple files
files1 = glob.glob('product/*.txt')

list1 = []
list2 = []
list3 = []
dict2 = {}
dict3 = {}
dict4 = {}
dict5 = {}
dict6 = {}


def stock():
    with open(file1, 'w') as f:
        for key, value in dict1.items():
            f.write('%s %d\n' % (key, value))  # %s shows where the string is to be specified


def stock_level():
    for file in files:
        try:
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
        except FileNotFoundError:
            print("The file doesn't exist")
    for key, value in dict3.items():
        print(key, value)


def product():
    index = random.randrange(0, len(files)+1)
    try:
        file_empty = files[index]
        with open(file_empty, 'r') as fr:
            lines = fr.readlines()
            for line in lines:
                list2.append(line.split())
    #    print(list2)
        x = int(list2[0][1]) // 2
        t = x // 2
        y = int(list2[1][1]) // 3
        z = int(list2[2][1]) // 2
        w = z // 4
        m = t + y + w
        n = x + w
        dict4['M'] = m
        dict4['N'] = n
        os.remove(file_empty)
    except IndexError as err:
        print(err)
    with open(file2, 'w') as fw:
        for k, v in dict4.items():
            fw.write(F'{k} {v}\n')


def product_level():
    for file3 in files1:
        with open(file3, 'r') as fs:
            lines = fs.readlines()
            for line in lines:
                list3.append(line.split())
        dict5.update(list3)
        for key, value in dict5.items():
            if key in dict6:
                dict6[key] += int(value)
            else:
                dict6[key] = int(value)
    for key, value in dict6.items():
        print(key, value)


def production():
    ratio = random.randint(1, 11)
    if ratio <= 4:
        return stock()
    else:
        return product()


def main():
    production()
    print('stock level: ')
    stock_level()
    print('product level: ')
    product_level()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
