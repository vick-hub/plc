import os
import sys


def main():
    with open("exotic.txt", "r+", encoding="utf-8") as f:
        f.read()
        f.write('exotic encoding')
#        print(f.tell())
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
