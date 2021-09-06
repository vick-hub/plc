import os
import sys


def main():
    x1, x2, x3, x4 = input("Enter values for x1, x2, x3, x4: ").split(",")
    y1, y2, y3, y4 = input("Enter values for y1, y2, y3, y4: ").split(",")
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    x4 = float(x4)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    y4 = float(y4)
    x = [[x1, x2], [x3, x4]]
    y = [[y1, y2], [y3, y4]]
    matrix_product = [(x[0][0] * y[0][0] + x[0][1] * y[1][0]), (x[0][0]*y[0][1] + x[0][1]*y[1][1])], [(x[1][0]*y[0][0] + x[1][1]*y[1][0]), (x[1][0]*y[0][1] + x[1][1]*y[1][1])]
    print(f" matrix solution = {matrix_product}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
