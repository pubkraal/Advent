#!/usr/bin/env python3

import sys
import time

from util.aoc import file_to_day
from util.input import load_grid


def main(test=False, animate=False):
    grid = load_grid(file_to_day(__file__), test)
    count = 0

    upper = 2000
    p1 = 0
    p2 = 0

    for i in range(upper):
        if animate:
            print_state(grid, i, count)
        grid = increment(grid)
        flashes, grid = flash(grid, None)
        count += flashes
        if i == 99:
            p1 = count
        if all(c == 0 for row in grid for c in row):
            if animate:
                print_state(grid, i + 1, count)
            p2 = i + 1
            break

    if animate:
        print("")
    print("2021:11:1 =", p1)
    print("2021:11:2 =", p2)


def increment(grid):
    gridlen = len(grid)
    for y in range(gridlen):
        for x in range(gridlen):
            grid[y][x] += 1
    return grid


def flash(grid, known=None):
    if known is None:
        known = set()
    flashset = set()
    flashes = 0
    gridlen = len(grid)
    for y in range(gridlen):
        for x in range(gridlen):
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
    if any([c > 9 for row in grid for c in row]):
        f, grid = flash(grid, known)
        flashes += f
    return flashes, grid


def print_state(grid, iteration, flashes):
    print("\033[H\033[2JIteration", iteration)
    print("Flashes:", flashes)
    print("")
    print_grid(grid)
    time.sleep(0.07)


def print_grid(grid):
    for line in grid:
        pline = "".join(map(str, line))
        print(pline.replace("0", "\033[1;37m0\033[0m"))


def get_adjacent(grid, y, x):
    coords = []
    gridlen = len(grid) - 1
    for py in range(y - 1, y + 2):
        if py < 0 or py > gridlen:
            continue
        for px in range(x - 1, x + 2):
            if px < 0 or px > gridlen:
                continue
            if px == x and py == y:
                continue
            coords.append((py, px))
    return coords


if __name__ == "__main__":
    test = "test" in sys.argv
    anim = "print" in sys.argv
    main(test, anim)
