import os
import sys


def main():
    # simple for
    for i in range(10):
        print(f"i = {i}")

    # <variable> can have multiple values 
    d = dict(zip(range(10), range(10, -0, -1)))
    print(d)
    print(d.items())
    for i, j in d.items():
        print(f"{i}->{j}")

    # continue
    d = dict(zip(range(10), range(10, 0, -1)))
    for i, j in d.items():
        if i == j:
            # skip
            continue
            # no code below will be run
        else:
            print(f"{i}->{j}")

    # break
    d = dict(zip(range(10), range(10, 0, -1)))
    for i, j in d.items():
        if i == j:
            # terminate loop
            break
        else:
            print(f"{i}->{j}")
    print("for exited")

    # for/else
    # else will be executed after for provide no break in for
    for i in range(10):
        if i == 5:
            # continue # else executed
            break  # else not executed
        print(f"i->{i}")
    else:
        print("for loop is done")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
