import os
import sys


def main():
    x1, x2, x3, x4, x5, x6, x7, x8, x9 = input("Enter values for x1,x2, x3, x4, x5, x6, x7, x8, x9: ").split(",")
    y1, y2, y3, y4, y5, y6, y7, y8, y9 = input("Enter values for y1, y2, y3, y4, y5, y6, y7, y8, y9: ").split(",")
    x1 = float(x1)
    x2 = float(x2)
    x3 = float(x3)
    x4 = float(x4)
    x5 = float(x5)
    x6 = float(x6)
    x7 = float(x7)
    x8 = float(x8)
    x9 = float(x9)
    y1 = float(y1)
    y2 = float(y2)
    y3 = float(y3)
    y4 = float(y4)
    y5 = float(y5)
    y6 = float(y6)
    y7 = float(y7)
    y8 = float(y8)
    y9 = float(y9)
    x = [[x1, x2, x3], [x4, x5, x6], [x7, x8, x9]]
    y = [[y1, y2, y3], [y4, y5, y6], [y7, y8, y9]]
    matrix_product = [(x[0][0]*y[0][0]+x[0][1]*y[1][0]+x[0][2]*y[2][0]), (x[0][0]*y[0][1]+x[0][1]*y[1][1]+x[0][2]*y[2][1]),
         (x[0][0]*y[0][2]+x[0][1]*y[1][2]+x[0][2]*y[2][2])], [(x[1][0]*y[0][0]+x[1][1]*y[1][0]+x[1][2]*y[2][0]),
          (x[1][0]*y[0][1]+x[1][1]*y[1][1]+x[1][2]*y[2][1]), (x[1][0]*y[0][2]+x[1][1]*y[1][2]+x[1][2]*y[2][2])], [(x[2][0]*y[0][0]+x[2][1]*y[1][0]+x[2][2]*y[2][0]), (x[2][0]*y[0][1]+x[2][1]*y[1][1]+x[2][2]*y[2][1]), (x[2][0]*y[0][2]+x[2][1]*y[1][2]+
        x[2][2]*y[2][2])]
    print(f"matrix solution = {matrix_product}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
