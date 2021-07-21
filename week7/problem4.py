import os
import sys
import pathlib


def main():
    new_dir = pathlib.Path("mars/mist")
    try:
        new_dir.mkdir()
    except OSError as error:
        print(error)
    new_file = pathlib.Path(new_dir, 'reduce-nut.txt')
    with open(new_file, 'w') as f:
        file = f.write('Hello, practicing working with files and path')
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
