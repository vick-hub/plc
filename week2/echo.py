import sys
import os

LENGTH = 24


def main():
    # the Python console
    # input()
    # s = input("s? ") # assign some value to variable s
    # print()
    # print(s, 9, 32, sep="")
    # print(type(s))
    print(1, 2, 3, 4, end="<<--!!-->>")
    print(1, 2, 3, 4)
    print(1, 2, 3, 4)
    # variable names
    # name = input("name: ")
    # age = input("age: ")
    number_of_games_lost = 32
    no_of_games_lost = 32
    num_of_games_lost = 23
    print(num_of_games_lost, type(num_of_games_lost))

    # keywords
    # good variable names
    # int, float, bool, str, None
    x = -32
    print(type(x))
    y = x * 2.982304982098302940238048029380
    print(type(y))
    print(y)
    print(round(y, 4))
    w = int('6')
    print(w, type(w))
    print(int('11', base=2))
    # 0-9,a-f
    print(int('ff', base=16))
    v = float('7.3328')
    print(v, type(v))
    print(float(1))
    print(False, type(False))
    print(True, type(True))
    b = bool(1)
    print(f"b = {b}", type(b))
    b = bool(0)
    print(f"b = {b}", type(b))
    b = bool(3)
    print(f"b = {b}", type(b))
    b = bool(-1)
    print(f"b = {b}", type(b))
    # 0 => False, Any number => True
    n = None
    print(n, type(n))
    # str methods
    s = 'this is' + " a string"
    print(s)
    S = """Write something interesting
    
    There is nothing to be concerned about.
    """
    print(S)
    s = f"My name is {'Paul'} and my age is {5}"
    print(s)

    v = 2323
    v_s = str(v)
    print(v_s, type(v_s))
    B = True
    N = None
    print(type(str(B)), type(str(N)))
    # split and distribution
    S = "Paul Korir"
    print(S, type(S))
    print(len(S))
    print(S.capitalize())
    print(S.upper())
    print(S.center(40, '!'))
    row = f"Paul Korir\t6/3/1942\tMumbai\t-\tPython\tCompany X"
    print(row)
    data = row.split("\t")
    print(data)
    print(type(data))
    name, dob, city, height, interest, work = row.split("\t")
    print(name)
    print(dob)
    print(city)
    print(height)
    print(interest)
    print(work)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
