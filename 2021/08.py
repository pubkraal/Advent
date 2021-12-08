#!/usr/bin/env python3

import sys
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
    segments = [frozenset(x) for x in feed.split() + r]
    digits = dict()

    # These are a given
    digits[1] = find_first_len(segments, 2)
    digits[4] = find_first_len(segments, 4)
    digits[7] = find_first_len(segments, 3)
    digits[8] = find_first_len(segments, 7)

    # These can be determined
    digits[0] = next(
        filter(
            lambda a: a & digits[4] != digits[4]
            and a & digits[7] == digits[7],
            find_len(segments, 6),
        )
    )
    digits[2] = next(
        filter(
            lambda a: a & digits[7] != digits[7] and len(a & digits[4]) != 3,
            find_len(segments, 5),
        )
    )
    digits[3] = next(
        filter(
            lambda a: a & digits[7] == digits[7],
            find_len(segments, 5),
        )
    )
    digits[5] = next(
        filter(
            lambda a: a & digits[7] != digits[7] and len(a & digits[4]) == 3,
            find_len(segments, 5),
        )
    )
    digits[6] = next(
        filter(
            lambda a: a & digits[4] != digits[4]
            and a & digits[7] != digits[7],
            find_len(segments, 6),
        )
    )
    digits[9] = next(
        filter(lambda a: a & digits[4] == digits[4], find_len(segments, 6))
    )

    lookup = {v: k for k, v in digits.items()}

    value = 0
    for n in r:
        value *= 10
        value += lookup[frozenset(n)]

    return value


def find_first_len(segments, length):
    return find_len(segments, length)[0]


def find_len(segments, length):
    return list(filter(lambda a: len(a) == length, segments))


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
