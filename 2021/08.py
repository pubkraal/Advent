#!/usr/bin/env python3

import sys
from itertools import permutations
from multiprocessing import Pool

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    uniq = 0
    lines = list(load_data(file_to_day(__file__), test))
    for line in lines:
        segments = line.strip().split(" | ")[1].split()
        uniq += sum([1 for x in segments if len(x) in (2, 3, 4, 7)])

    pool = Pool(8).map(calc, lines)

    print("2021:08:1 =", uniq)
    print("2021:08:2 =", sum(pool))


def calc(line):
    feed, end = line.strip().split(" | ")
    return output(feed, end)


def output(feed, result):
    r = result.split()
    segments = feed.split() + r
    fs = frozenset
    for a, b, c, d, e, f, g in permutations(range(7)):
        digits = {
            fs((a, b, c, e, f, g)): 0,
            fs((c, f)): 1,
            fs((a, c, d, e, g)): 2,
            fs((a, c, d, f, g)): 3,
            fs((b, c, d, f)): 4,
            fs((a, b, d, f, g)): 5,
            fs((a, b, d, e, f, g)): 6,
            fs((a, c, f)): 7,
            fs((a, b, c, d, e, f, g)): 8,
            fs((a, b, c, d, f, g)): 9,
        }
        found = test_key(segments, digits)
        if not found:
            continue

        value = 0
        for x in r:
            value = (value * 10) + digits[build_key(x)]
        return value


def test_key(segments, digits):
    for x in segments:
        if build_key(x) not in digits:
            return False
    return True


def build_key(numbers):
    return frozenset(line - ord("a") for line in numbers.encode())


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
