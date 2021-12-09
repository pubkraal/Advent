#!/usr/bin/env python3

import sys
from functools import reduce

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    hmap = [
        list(map(int, line.strip()))
        for line in load_data(file_to_day(__file__), test)
    ]

    lowest = get_lowest_points(hmap)
    basins = get_basins(hmap)
    print("2021:09:1 =", sum([p + 1 for p in lowest]))
    print(
        "2021:09:2 =",
        reduce(lambda a, b: a * b, list(sorted(basins, reverse=True))[:3]),
    )


def get_basins(hmap):
    basins = []
    mmap = hmap[:]
    for y in range(len(mmap)):
        for x in range(len(mmap[y])):
            p = mmap[y][x]
            if p == "x":
                continue
            if p < 9:
                basins.append(collect_basin(mmap, y, x))
    return basins


def collect_basin(mmap, sy, sx):
    hmap = mmap[:]
    count = 1
    hmap[sy][sx] = "x"

    adj = filter(
        lambda c: hmap[c[0]][c[1]] not in ("x", 9),
        get_adjacent_coord(hmap, sx, sy),
    )
    for p in adj:
        count += collect_basin(mmap, p[0], p[1])

    return count


def get_lowest_points(hmap):
    lowest = []
    h = len(hmap)
    w = len(hmap[0])
    for y in range(h):
        for x in range(w):
            p = hmap[y][x]
            adj = get_adjacent(hmap, x, y)
            if all(p < a for a in adj):
                lowest.append(p)

    return lowest


def get_adjacent_coord(hmap, x, y):
    adj = []
    if x > 0:
        adj.append((y, x - 1))
    if y > 0:
        adj.append((y - 1, x))
    if x < len(hmap[0]) - 1:
        adj.append((y, x + 1))
    if y < len(hmap) - 1:
        adj.append((y + 1, x))
    return adj


def get_adjacent(hmap, x, y):
    adj = []
    if x > 0:
        adj.append(hmap[y][x - 1])
    if y > 0:
        adj.append(hmap[y - 1][x])
    if x < len(hmap[0]) - 1:
        adj.append(hmap[y][x + 1])
    if y < len(hmap) - 1:
        adj.append(hmap[y + 1][x])
    return adj


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
