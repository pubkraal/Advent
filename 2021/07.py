#!/usr/bin/env python3

import sys
from functools import cache

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    positions = list(
        map(int, load_data(file_to_day(__file__), test)[0].strip().split(","))
    )

    minfuel = float("inf")
    minfuel2 = float("inf")
    for x in range(min(positions), max(positions)):
        steps = [abs(p - x) for p in positions]
        distance = sum(steps)
        distance2 = sum([fuel_cost(x) for x in steps])
        minfuel = min(distance, minfuel)
        minfuel2 = min(distance2, minfuel2)

    print("2021:07:1 =", minfuel)
    print("2021:07:2 =", minfuel2)


@cache
def fuel_cost(distance):
    return sum(list(range(1, distance + 1)))


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
