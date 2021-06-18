import sys
import os


def main():
    # simple for
    # for i in range(10):
    #     print(f"i = {i}")

    # <variable> can have multiple values 
    # d = dict(zip(range(10), range(9, -1, -1)))
    # for i, j in d.items():
    #     print(f"{i}->{j}")

    # continue
    # d = dict(zip(range(10), range(10, 0, -1)))
    # for i, j in d.items():
    #     if i == j:
    #         # skip
    #         continue
    #     else:
    #         print(f"{i}->{j}")
            
    # break
    # d = dict(zip(range(10), range(10, 0, -1)))
    # for i, j in d.items():
    #     if i == j:
    #         # terminate loop
    #         break
    #     else:
    #         print(f"{i}->{j}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())