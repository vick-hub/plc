import os
import sys


def main():
    # NameError: variable doesn't exist
    # print(s)
    # ValueError
    # print(int('s'))
    # TypeError
    # print('s' + 1)
    # SyntaxError
    # def lsdkjfldkj()
    # print(1 + 2)
    # IndexError
    l = list(range(10))
    # l[14]
    # catching exceptions
    try:
        v = l[14]
    except IndexError as ie:
        print(f"warning: {ie}; list too short")
        v = 0
    print(f"v = {v}")
    # catching multiple exceptions
    try:
        v = 's' + l[4]
    except IndexError as ie:
        print(f"warning: {ie}; list too short")
        v = 's0'
    except TypeError as te:
        print(f"warning: {te}; not the right type")
        v = 's0'
    except ValueError as ve:
        print(f"warning: {ve}; wrong value")
        v = 's0'
    print(f"v = {v}")
    # raising exceptions
    # raise TypeError('something went wrong')
    # assertions
    age = int(input("your age? "))
    try:
        assert 0 < age < 120 # if True no exception; otherwise special exception
    except AssertionError:
        print(f"error: invalid age {age}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
