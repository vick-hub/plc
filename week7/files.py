import os
import sys


def main():
    # official dox: https://docs.python.org/3/tutorial/inputoutput.html#tut-files
    # vanilla file handling
    # f = open(<filename>, <mode>, ...)
    # print(f)
    # print(type(f))
    # f.close()

    # file opening modes
    # 'r', 'w', 'a', 'b', 't'
    # war_and_peace.txt
    # image.jpg
    # example of appending to a file

    # with context manager
    # to cleanly handle closing of files

    # reading data
    # f.read() -> everything
    # f.readline() -> str
    # f.readlines() -> list

    # writing to a file
    # f.write()
    # print("something", file=<file_object>)

    # navigating through a file
    # f.tell()
    # f.seek()

    # exceptions
    # FileExistsError
    # FileNotFoundError
    # see the notes for more errors

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
