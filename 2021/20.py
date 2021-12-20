#!/usr/bin/env python3

import sys

from util.aoc import file_to_day
from util.input import load_data

INC = 8


def main(test=False):
    data = load_data(file_to_day(__file__), test)
    filter_ = [c for c in data[0]]
    image = set()
    for y, row in enumerate(data[2:]):
        for x, cell in enumerate(row):
            if cell == "#":
                image.add((x, y))

    p1 = 0
    for x in range(50):
        if x == 2:
            p1 = len(image)
        on = x % 2 == 0
        image = transpose(image, on, filter_)

    print("2021:20:1 =", p1)
    print("2021:20:2 =", len(image))


def transpose(image, default, noisefilter):
    ymin = min([y for _, y in image])
    ymax = max([y for _, y in image])
    xmin = min([x for x, _ in image])
    xmax = max([x for x, _ in image])

    ni = set()

    for y in range(ymin - 5, ymax + 10):
        for x in range(xmin - 5, xmax + 10):
            index = 0
            bit = 8
            for coord in get_coords(x, y):
                if ((coord[0], coord[1]) in image) == default:
                    index += 2 ** bit
                bit -= 1
            if (noisefilter[index] == "#") != default:
                ni.add((x, y))

    return ni


def get_coords(x, y):
    return [(x + tx, y + ty) for ty in (-1, 0, 1) for tx in (-1, 0, 1)]


def print_image(image):
    ymin = min([y for _, y in image])
    ymax = max([y for _, y in image])
    xmin = min([x for x, _ in image])
    xmax = max([x for x, _ in image])

    for y in range(ymin, ymax + 1):
        for x in range(xmin, xmax + 1):
            print("#" if (x, y) in image else ".", end="")
        print("")


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
