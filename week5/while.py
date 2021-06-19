import os
import sys


def main():
    # simple while
    i = 0
    while i < 10:  # as long as this is True we loop
        print(f"i = {i}")
        # modify the value i
        # whenever <assign_expr> has '<' then i has to be incremented
        i += 1
    print(f"value of i after while: {i}")

    # reverse looping
    while i >= 0:
        print(f"i = {i}")
        i -= 2
    print(f"value of i after while: {i}")

    # while with container
    my_list = list(range(10))
    print(my_list)
    while my_list:  # treated as with integers; eval the length: 0->False; !=0->True
        print(my_list[-1])  # last value
        print(f"length of my_list is {len(my_list)}")
        my_list.pop()
    print(my_list)

    # continue
    i = 0
    while i < 10:  # < implies +
        if i == 5:
            # adjust i; skip
            print(f"skipping {i}...")
            i += 1
            continue
        print(f"i = {i}")
        i += 1

    # break
    my_list = list(range(10))
    while my_list:
        if my_list[-1] == 3:
            # terminate
            break
        print(my_list[-1])
        my_list.pop()
    print(my_list)

    # while/else
    i = 0
    while i < 10:
        print(f"i-->{i}")
        if i == 4:
            i += 2
            # continue # else will be executed
            break  # else will not be executed
        i += 2
    else:
        print("the else is executed")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
