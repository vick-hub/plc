import os
import sys

# fixme: can you think of a better name for this function?
def gravitational_law(m1, m2, r, g=10):
    # todo: docstring
    f = float(g * ((m1 * m2) / r ** 2))
    return f


def main():
    try:
        m1 = float(input("m1: "))
        m2 = float(input("m2: "))
        r = float(input("r : "))
        # fixme: you can use round() to round the number of digits
        print(f"Force = {gravitational_law(m1, m2, r)}N")
    except ZeroDivisionError as err:
        print(f"Handling runtime error:", err)
    except ValueError as val:
        print("Oops! is not valid number: ", val)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
