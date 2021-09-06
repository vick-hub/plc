import os
import sys


def main():
    k = list(range(3, 12))
    print(f"values in descending order: {k[::-1]}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
