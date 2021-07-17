import os
import sys
import struct
import random


def main():
    with open('binary_integer.bin', 'wb') as f:
        data = struct.pack('i', 1)
        f.write(data)
    #    print(data)
        size = struct.calcsize('i')
        print("size in bytes: {}".format(size))

    with open('binary_integers.bin', 'wb') as f:
        integers_1000 = random.choices(range(1000), k=1000)
        for integer in integers_1000:
            data = struct.pack('f', integer)
            f.write(data)
            print(data)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
