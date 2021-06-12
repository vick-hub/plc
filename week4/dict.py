import os
import sys
import random
import string


def main():
    # 1. creating dictionaries
    d = dict()  # class
    print(d, type(d))
    d2 = {"triangle": 'a', "circle": 'b'}  # literal
    print(d2, type(d2))
    d3 = dict(triangle='a', circle='b')  # kwargs
    print(d3, type(d3))
    d4 = dict({"triangle": 'a', "circle": 'b'}, square='d', rectangle='e')  # mix and match
    print(d4, type(d4))
    keys = random.choices(range(10), k=10)
    values = random.choices(range(10), k=10)
    print(f"keys = {keys}")
    print(f"values = {values}")
    print(list(zip(keys, values)))  # zip
    d5 = dict([(8, 2), (0, 9), (1, 6), (3, 1), (2, 1), (2, 2), (6, 9), (7, 3), (2, 0), (2, 2)])
    print(d5)
    d6 = dict(zip(keys, values))
    print(d6)
    d7 = dict(zip(string.ascii_lowercase, values))
    print(d7)
    #
    # # 2. retrieving items from dictionaries
    # print(d7['a'])
    # print(d[3])
    print(d6)
    try:
        print(f"value with key = 3 is {d6[3]}")
    except KeyError:
        print(f"default value is 999")
    # # d.get(key, [default])
    print(f"default value is {d6.get(3, 999)}")
    # # d[key]
    # # KeyError
    #
    # 3. modifying dict content
    # d[key] = value
    shapes = {
        'triangle': 234,
        'circle': 9893,
        'square': 3782,
        'rectangle': 993,
        'rhombus': 232,
        'trapezium': 93,
    }
    print(shapes)
    shapes['circle'] = 555
    print(shapes)
    # d.setdefault(key, [default])
    shapes['oval'] = 777
    print(shapes)
    # print(shapes['diamond'])
    print("diamond has ", shapes.setdefault('diamond', 464))
    print(shapes)
    # crud: create, read, update and delete
    # del d[key]
    del shapes['square']
    print(shapes)

    # 4. membership (key in, key not in)
    print("Is square in shapes?", 'square' in shapes)  # False
    print("Is oval in shapes?", 'oval' in shapes)  # True
    print("Is square not in shapes?", 'square' not in shapes)  # True

    # 5. castings/function on dict
    # len(d)
    print(len(shapes))
    # iter(d) -> iterator over keys of dict
    print(iter(shapes))
    for k in iter(shapes):
        print(f"key = {k}")
    # list(d)
    print(shapes)
    print(list(shapes))  # only keys

    # 6. dict methods
    # dict.get(key, [default])
    # dict.setdefault(key, [default])
    # # dict.items()
    # for x in shapes:
    #     print(x, shapes[x])
    print(shapes.items())
    for key, value in shapes.items():
        print(f"The shape {key} has areas {value}")
    # dict.keys()
    print(f"Keys: {shapes.keys()}")
    # dict.values()
    print(f"Value: {shapes.values()}")
    # # lists as values
    fancy = dict()
    fancy[(0, 0)] = random.choices(range(10), k=3)
    fancy[(0, 1)] = random.choices(range(10), k=3)
    fancy[(1, 0)] = random.choices(range(10), k=3)
    fancy[(1, 1)] = random.choices(range(10), k=3)
    print(fancy)
    # # dict.update()
    fancy2 = dict()
    fancy2[(1, 1)] = random.choices(range(10), k=3)
    fancy2[(1, 2)] = random.choices(range(10), k=3)
    fancy2[(2, 2)] = random.choices(range(10), k=3)
    print(fancy2)
    fancy.update(fancy2)
    print(fancy)
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
