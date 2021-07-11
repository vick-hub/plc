import os
import pathlib
import sys


def main():
    # official documentation: https://docs.python.org/3/library/pathlib.html
    # import the pathlib library
    # creating Path objects
    path = pathlib.Path('.')
    print(path, type(path))

    # using the / operator: https://docs.python.org/3/library/pathlib.html#operators
    new_path = path / "some_file.txt"
    print(new_path, type(new_path))

    # methods: https://docs.python.org/3/library/pathlib.html#operators
    # Path.name
    print(new_path.name)
    # Path.parent
    print(new_path.parent)
    print(new_path.absolute())
    # Path.exists()
    other_path = pathlib.Path("./nothing.txt")
    print(other_path)
    print(other_path.exists())
    with other_path.open('w') as f:
        f.write("there is nothign here\n")
    print(other_path.exists())
    other_path.unlink()
    # Path.is_dir()
    print(other_path.is_dir())

    # Path.mkdir() analogous to mkdir in Linux
    new_dir = pathlib.Path("./chips")
    print(new_dir.exists())
    new_dir.mkdir()
    print(new_dir.exists())

    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
