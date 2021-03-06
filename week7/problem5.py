import os
import sys
import pathlib


def main():
    path = pathlib.Path('cortex')
    print(path)
    try:
        os.mkdir(path)
    except OSError:
        pass
    path1 = path/'nothing.txt'
    print(path1)
    with open(path/'nothing.txt', 'r') as f:
        f.read()
    path2 = path/'image.jpg'
    print(path2)
    with open(path/'image.jpg', 'rb') as f:
        f.read()
    path3 = path/'orange.json'
    print(path3)
    path4 = '/home/victor/path'
    print(path4)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
