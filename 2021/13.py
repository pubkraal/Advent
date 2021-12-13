#!/usr/bin/env python3

import sys

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    dotdata = []
    instructions = []
    data = load_data(file_to_day(__file__), test)
    for idx, line in enumerate(data):
        if line == "":
            dotdata = data[:idx]
            instructions = data[idx + 1 :]
            break

    dots = set(tuple(map(int, n.split(","))) for n in dotdata)

    for idx, inst in enumerate(instructions):
        dots = fold_grid(dots, inst.split(" ")[-1])
        if idx == 0:
            p1 = len(dots)

    print("2021:13:1 =", p1)
    print("2021:13:2 =")
    print_grid(dots)


def fold_grid(dots, pos):
    axis, coord = pos.split("=")
    coord = int(coord)

    new = set()
    for dot in dots:
        index = "xy".index(axis)
        if dot[index] < coord:
            new.add(dot)
        else:
            offset = coord * 2
            if index == 0:
                new.add((offset - dot[0], dot[1]))
            else:
                new.add((dot[0], offset - dot[1]))
    return new


def print_grid(dots):
    maxx = max([d[0] for d in dots])
    maxy = max([d[1] for d in dots])
    for y in range(maxy + 1):
        for x in range(maxx + 1):
            if (x, y) in dots:
                print("#", end="")
            else:
                print(" ", end="")
        print()


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
