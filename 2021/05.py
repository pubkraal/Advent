#!/usr/bin/env python3

import sys
from collections import defaultdict

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    vents = defaultdict(int)
    dvents = defaultdict(int)
    for line in load_data(file_to_day(__file__), test):
        l, r = line.strip().split(" -> ")
        y, x = map(int, l.split(","))
        y2, x2 = map(int, r.split(","))
        if y == y2:
            s = min(x, x2)
            e = max(x, x2)
            for i in range(s, e + 1):
                vents[(y, i)] += 1
                dvents[(y, i)] += 1
        elif x == x2:
            s = min(y, y2)
            e = max(y, y2)
            for i in range(s, e + 1):
                vents[(i, x)] += 1
                dvents[(i, x)] += 1
        elif abs(x - x2) == abs(y - y2):
            s = get_step(y, x, y2, x2)
            ty, tx = y, x
            dvents[(ty, tx)] += 1
            while (ty, tx) != (y2, x2):
                ty += 1 * s[0]
                tx += 1 * s[1]
                dvents[(ty, tx)] += 1

    overlap = sum(v > 1 for v in vents.values())
    overlap2 = sum(v > 1 for v in dvents.values())

    print("2021:05:1 =", overlap)
    print("2021:05:2 =", overlap2)


def get_step(y, x, y2, x2):
    ystep, xstep = 1, 1
    if y2 < y:
        ystep = -1
    if x2 < x:
        xstep = -1

    return (ystep, xstep)


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
