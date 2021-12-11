#!/usr/bin/env python3

import sys

from util.aoc import file_to_day
from util.input import load_grid


def main(test=False):
    grid = load_grid(file_to_day(__file__), test)
    count = 0

    upper = 2000

    for i in range(upper):
        grid = increment(grid)
        flashes, grid = flash(grid, None)
        count += flashes
        if i == 99:
            print("2021:11:1 =", count)
        if all(c == 0 for l in grid for c in l):
            print("2021:11:2 =", i+1)
            break


def increment(grid):
    l = len(grid)
    for y in range(l):
        for x in range(l):
            grid[y][x] += 1
    return grid


def flash(grid, known=None):
    if known is None:
        known = set()
    flashset = set()
    flashes = 0
    l = len(grid)
    for y in range(l):
        for x in range(l):
            if grid[y][x] > 9:
                grid[y][x] = 0
                flashes += 1
                flashset.add((y, x))

    known.update(flashset)

    for (x, y) in flashset:
        for ay, ax in get_adjacent(grid, x, y):
            if (ay, ax) in known:
                continue

            grid[ay][ax] += 1
    if any([c > 9 for l in grid for c in l]):
        f, grid = flash(grid, known)
        flashes += f
    return flashes, grid


def print_grid(grid):
    for line in grid:
        print("".join(map(str, line)))


def get_adjacent(grid, y, x):
    coords = []
    l = len(grid) - 1
    for py in range(y-1, y+2):
        if py < 0 or py > l:
            continue
        for px in range(x-1, x+2):
            if px < 0 or px > l:
                continue
            if px == x and py == y:
                continue
            coords.append((py, px))
    return coords

if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
