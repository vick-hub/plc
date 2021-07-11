import os
import sys


def main():
    # official dox: https://docs.python.org/3/tutorial/inputoutput.html#tut-files
    # vanilla file handling
    # f = open(<filename>, <mode>, ...)
    f = open("war_and_peace.txt")
    print(f)
    print(f"the type of file is: ", type(f))
    f.close()

    # file opening modes
    # 'r', 'w', 'a', 'b', 't'
    # war_and_peace.txt
    # image.jpg
    f = open("image.jpg", 'rb')
    print(type(f))
    f.close()
    # example of appending to a file
    f = open("my_file.txt", 'w')
    f.write("hello")
    f.close()

    f = open("my_file.txt", 'a')
    f.write(" world\n")
    f.close()

    # with context manager
    # to cleanly handle closing of files
    """
    f = open("file.txt")
    # line 1
    # line 2
    # ...
    # line 100
    f.close()
    """
    with open("my_file.txt") as f:
        print(f)

    # reading data
    # f.read() -> everything, str
    with open("war_and_peace.txt") as f:
        data = f.read()
        print(f"f.read(): {len(data)}")
        print(data[:100])
    # f.readline() -> str
    with open("war_and_peace.txt") as f:
        data = f.readline()
        print(f"f.readline(): {data}")
    # f.readlines() -> list
    with open("war_and_peace.txt") as f:
        data = f.readlines()
        print(f"f.readlines(): {len(data)}")
        print(data[:5])
    # writing to a file
    # f.write()
    # print("something", file=<file_object>)
    with open("some_file.txt", 'w') as f:
        f.write("This eBook is for the use of anyone a\n")
        print("The Project Gutenberg eBook of War and Peace, by Leo Tolstoy", file=f)

    # navigating through a file
    # f.tell() "where am I in the file?"
    # f.seek() "go to a particular location"
    with open("some_file.txt", 'a') as f:
        # where are we?
        print(f"we are at position: {f.tell()}")
        f.seek(0)
        print(f"we are at position: {f.tell()}")
        f.write("hello world\n")

    with open("some_file.txt", 'r+') as f:
        # where are we?
        print(f"we are at position: {f.tell()}")
        f.seek(0)
        print(f"we are at position: {f.tell()}")
        f.write("hello world\n")

    # f.tell() and f.seek() help to renavigate after reading through

    # exceptions
    # FileNotFoundError
    # with open("non_existent_file.txt") as f:
    #     print(f)
    # FileExistsError
    # with open("some_file.txt", 'x') as f:
    #     print(f)
    # see the notes for more errors

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
