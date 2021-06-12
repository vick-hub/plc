import os
import sys


def main():
    # 1. creating dictionaries

    # 2. retrieving items from dictionaries
    # d[key]
    # d.get(key, [default])
    # KeyError

    # 3. modifying dict content
    # d[key] = value
    # d.setdefault(key, [default])
    # del d[key]

    # 4. membership (key in, key not in)

    # 5. castings on dict
    # len(d)
    # iter(d)
    # list(d)

    # 6. dict methods
    # dict.get(key, [default])
    # dict.setdefault(key, [default])
    # dict.items()
    # dict.keys()
    # dict.values()
    # dict.update()
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
