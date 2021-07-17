import os
import sys
import pathlib


def main():
    new_dir = pathlib.Path("mars/mist")
    new_dir.mkdir()
    print(new_dir.exists())
    with open('reduce-nut.txt', 'r+') as f:
        print(f.read())
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
