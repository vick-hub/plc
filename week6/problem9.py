import os
import sys
import math

"""
Notes:
- Good attempt!
- Make the functions for equations of motion return the value they calculate
- 
"""
def equations_of_motion(vo, a, t):
    v = float(vo + (a * t))
    return v


def equations_of_motion1(vo, a, ro, r):
    # todo: docstring
    v1 = math.sqrt((vo ** 2) + (2 * a * (r - ro)))
    return v1


functions = {1: equations_of_motion, 2: equations_of_motion1}
print(f"which function will you use to solve for v: ")


def main():
    for k, v in functions.items():
        print(v, '=', k)
    selected = input('Enter the function 1 or 2: ')
    for i in selected:
        vo = float(input("vo: "))
        a = float(input("a: "))
        t = float(input("t: "))
        if i == 1:
            # fixme: your functions have no return so they return None
            print(f"v: {equations_of_motion(vo, a, t)}")
        else:
            ro = float(input("ro: "))
            r = float(input("r: "))
            print(equations_of_motion1(vo, a, ro, r))
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
