#!/usr/bin/env python3

import sys
from functools import cache
from statistics import median, mean

from util.aoc import file_to_day
from util.input import load_ints


def main(test=False):
    positions = load_ints(file_to_day(__file__), test)

    m = int(median(positions))
    print("2021:07:1 =", sum([abs(x - m) for x in positions]))
    m2 = int(round(mean(positions)))

    # round is inaccurate, test surrounding numbers
    p2_min = float("inf")
    for t in range(m2 - 1, m2 + 2):
        p2_min = min(sum([fuel_cost(abs(x - t)) for x in positions]), p2_min)
    print("2021:07:2 =", p2_min)


@cache
def fuel_cost(distance):
    return distance * (distance + 1) // 2


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
