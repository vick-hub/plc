import math
import os
import random
import sys


def calculate(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(discriminant)) / 2 / a
    x2 = (-b - math.sqrt(discriminant)) / 2 / a
    return x1, x2


def add(number, extra=5):
    print(f"number = {number}")
    print(f"extra = {extra}")
    return number + extra


A = 10


def do_something(a):
    # A = 1
    global A
    A = A + a
    return A


def f(a, b, c=5, d=8):
    print(f"a = {a}")
    print(f"b = {b}")
    return a * b - a * c + b * d


def add_two(number1, number2):
    return number1 + number2


def main():
    # example 1
    # invoke the function
    x1, x2 = calculate(1, 2, 1)  # unpacking of a tuple
    print(f"x1 = {x1}; x2 = {x2}")

    # example 2
    bigger1 = add(1)  # OK
    print(f"bigger1 = {bigger1}")
    bigger2 = add(1, 3)  # don't do this!!!
    print(f"bigger2 = {bigger2}")
    bigger3 = add(3, 1)  # don't do this!!!
    print(f"bigger3 = {bigger3}")
    bigger4 = add(1, extra=3)  # the right way to call add()
    print(f"bigger4 = {bigger4}")
    bigger5 = add(number=1, extra=3)  # don't do this!!!
    print(f"bigger5 = {bigger5}")

    # global vs. local scope
    print(f"A = {A}")  # global A
    a2 = do_something(3)  # modified global A
    print(f"a2 = {a2}")
    print(f"A = {A}")

    # positional parameters
    # x0 = f(1) # Error!
    # x1 = f(b=7) # Error!
    x2 = f(3, 7)  # OK, with defaults
    x3 = f(b=8, a=3)  # misleading, NOK

    # default parameters
    # x0 = f(c=6, d=12) # Error!
    # x1 = f(c=6, d=12, 1, 2) # Error!
    x2 = f(1, 2, d=12)  # OK, modifying one of the defaults
    x3 = f(1, 2, 3, 4)  # don't do this!!! misleading

    # anonymous functions
    print(f)  # what is the type of f
    print(type(f))
    print(lambda x: x ** 2)  # only take one statement
    square = lambda x: x ** 2
    print(square)

    # map()
    rands = random.choices(range(10), k=15)
    print(rands)
    square = list()
    for r in rands:
        square.append(r ** 2)
    print(square)
    # one line using map
    square_mapped = list(map(lambda x: x ** 2, rands))
    print(square_mapped)

    N1 = random.choices(range(10), k=15)
    N2 = random.choices(range(10), k=15)
    # map takes the name of the function (without parentheses)
    Nsum = list(map(add_two, N1, N2))
    print(N1)
    print(N2)
    print(Nsum)
    print(list(map(add_two, N1, N2[:-3])))

    # filter()
    rands = random.choices(range(10), k=15)
    print(rands)
    # function must return something that can be evaluated to a bool
    # True, False, None, <integer>, container
    # if True include
    odd_rands = list(filter(lambda x: bool(x % 2), rands))
    even_rands = list(filter(lambda x: not bool(x % 2), rands))
    print(odd_rands)
    print(even_rands)
    # equivalent for filter, odds
    odds = list()
    for r in rands:
        if r % 2 == 1:
            if True:
                print()
            odds.append(r)
    print(odds)

    # the following line illustrates that the function definition doesn't not have to
    # precede the function call; test_something() is defined below 👇
    test_something(32)

    return os.EX_OK


def test_something(i):
    print(f"this is {i}")


if __name__ == "__main__":
    sys.exit(main())
