import sys
import os


def main():
    # simple while
    # i = 0
    # while i < 10:
    #     print(f"i = {i}")
    #     i += 1

    # while with container
    # my_list = list(range(10))
    # while my_list:
    #     print(my_list[-1])
    #     my_list.pop()

    # continue
    # i = 0
    # while i < 10:
    #     if i == 5:
            # adjust i; skip
            # i += 1
            # continue
        # print(f"i = {i}")
        # i += 1

    # break
    # my_list = list(range(10))
    # while my_list:
    #     if my_list[-1] == 3:
            # terminate
            # break
        # print(my_list[-1])
        # my_list.pop()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())