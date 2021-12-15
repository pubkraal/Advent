#!/usr/bin/env python3

import sys
import heapq

from util.aoc import file_to_day
from util.input import load_grid


def main(test=False):
    data = load_grid(file_to_day(__file__), test)

    print("2021:15:1 =", find_path(data))
    print("2021:15:2 =", find_path(data, 5))


def find_path(grid, dupes=1):
    row_dir = [-1, 0, 1, 0]
    col_dir = [0, 1, 0, -1]
    h = len(grid)
    w = len(grid[0])

    resgrid = [[None for _ in range(dupes * w)] for _ in range(dupes * h)]
    heap = [(0, 0, 0)]
    while heap:
        (distance, row, col) = heapq.heappop(heap)
        if row < 0 or row >= dupes * h or col < 0 or col >= dupes * w:
            continue

        val = (grid[row % h][col % w] + (row // h) + (col // w)) % 9
        cost = distance + val

        if resgrid[row][col] is None or cost < resgrid[row][col]:
            resgrid[row][col] = cost
        else:
            continue

        if row == dupes * h - 1 and col == dupes * w - 1:
            break

        for i in range(4):
            nr = row + row_dir[i]
            nc = col + col_dir[i]
            heapq.heappush(heap, (resgrid[row][col], nr, nc))
    return resgrid[dupes * h - 1][dupes * w - 1] - grid[0][0]


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
