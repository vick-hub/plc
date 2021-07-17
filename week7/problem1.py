import os
import sys


def main():
    with open('war_and_peace.txt', 'r') as f:
        for line in f:
            line = line.strip()
            print(line)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
