import os
import sys


def main():
    # official documentation: https://docs.python.org/3/library/pathlib.html
    # import the pathlib library
    # creating Path objects

    # using the / operator: https://docs.python.org/3/library/pathlib.html#operators

    # methods: https://docs.python.org/3/library/pathlib.html#operators
    # Path.name
    # Path.parent
    # Path.exists()
    # Path.is_dir()

    # Path.mkdir() analogous to mkdir in Linux
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
