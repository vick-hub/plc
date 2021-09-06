import os
import sys
import math


def main():
    x1 = int(input("x1: "))
    x2 = int(input("x2: "))
    y1 = int(input("y1: "))
    y2 = int(input("y2: "))
    z1 = int(input("z1: "))
    z2 = int(input("z2: "))
    d = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)
    print(f"Distance between A(x1, y1, z1) and B(x2, y2, z2): D = {d}")
    e = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance between origin(0, 0, 0) and A(x1, y1, z1): E = {e}")
    f = math.sqrt(x2 ** 2 + y2 ** 2 + z2 ** 2)
    print(f"Distance between origin(0, 0, 0) and B(x2, y2, z2): F = {f}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
