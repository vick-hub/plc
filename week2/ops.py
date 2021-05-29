import sys
import os


def main():
    # operators: +, -, *, /, parentheses
    x = 1
    y = 2
    print(x + y)
    print(x * y)
    print(x / y)
    print(x - y)
    # BODMAS - brackets of division multiplication addition subtraction
    z = 7
    print(x + y * z)
    print((x + y) * z)
    print(2 // 7) # integer division
    print(2 % 7) # modulo operator
    # numeric
    # str
    print('lskdjfldj' + '1!!!!!!')
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
