import os
import sys
import random


def main():
    file1 = open("input_matrices.txt", 'r')
    file2 = open("matrix_products.txt", 'w')
    content = file1.readlines()
    type(content)
    for r in content:
        r = r.strip()
        matrix_product = ([r[0] * r[9] + r[1] * r[12] + r[2] * r[15], r[0] * r[10] + r[1] * r[13] + r[2] * r[16],
                           r[0] * r[11] + r[1] * r[14] + r[2] * r[17]],
                          [r[3] * r[9] + r[4] * r[12] + r[5] * r[15], r[3] * r[10] + r[4] * r[13] + r[5] * r[16],
                           r[3] * r[11] + r[4] * r[14] + r[5] * r[17]],
                          [r[6] * r[9] + r[7] * r[12] + r[8] * r[15], r[6] * r[10] + r[7] * r[13] + r[8] * r[16],
                           r[6] * r[11] + r[7] * r[14] + r[8] * r[17]])
        file2.write(matrix_product)
#        print(f"matrix_products: {matrix_product}")
    file1.close()
    file2.close()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
