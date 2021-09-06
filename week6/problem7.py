import os
import sys
import math


def distance_two(coordinates):
    distance = 0
    ox, oy, oz = coordinates[0]
    for x, y, z in coordinates[1:]:
        # good use of pow(...)
        distance += math.sqrt(pow(ox - x, 2) + pow(oy - y, 2) + pow(oz - z, 2))
        ox, oy, oz = x, y, z
    return distance


def main():
    # fixme: NameError when I enter 'a, b, c'
    x1, y1, z1 = eval(input('Enter coordinates of point1 x,y,z: '))
    x2, y2, z2 = eval(input('Enter coordinates of point2 x,y,z: '))
    print(f"Distance between 2 points: {distance_two(coordinates=((x1, y1, z1), (x2, y2, z2)))}")
    # fixme: try to avoid doing this 👇
    #   this is what variables are for; just use a variable and put it in the string!
    print(f"Perimeter of irregular polygon: {distance_two(coordinates=((1, 3, 2), (3, 1, 5), (5, 2, 1), (4, 5, 4), (2, 4, 3), (1, 3, 2)))}")
    return os.EX_OK


if __name__ == "__main__":
    sys.exit(main())
