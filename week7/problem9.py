import os
import sys
import struct


def main():
    sum_s = 0
    with open("sensor.bin", 'rb') as f:
        for number in f:
            data = struct.unpack('i', number)
            for integer in data:
                sum_s += integer
                print(f"Sum of readouts: {sum_s}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
