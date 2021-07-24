import os
import sys


def main():
    with open("exotic.txt", "r", encoding="koi8-r") as fr:
        with open('new_file.txt', 'w+', encoding='utf-8') as ft:
            for line in fr:
                ft.write(line[:-1] + '\r\n')  # select all but leaves the last newline
                ft.read()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
