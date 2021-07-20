import os
import sys
import pathlib


def main():
    path = pathlib.Path('cortex')
    print(path)
    path1 = pathlib.Path('cortex/nothing.txt')
    print(path1)
    path2 = pathlib.Path('cortex/image.jpg')
    print(path2)
    path3 = pathlib.Path('cortex/orange.json')
    print(path3)
    path4 = pathlib.Path('/cortex')
    print(path4)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
