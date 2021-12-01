#!/usr/bin/env python3

from util.aoc import file_to_day
from util.input import load_data


def main():
    n = [int(x.strip()) for x in load_data(file_to_day(__file__))]
    sums = [sum(n[i : i + 3]) for i in range(0, len(n) - 2)]

    print("2021:01:1 =", get_incs(n))
    print("2021:01:2 =", get_incs(sums))


def get_incs(iter):
    numinc = 0
    prev = None

    for cur in iter:
        if prev is None:
            prev = cur
            continue

        numinc += cur > prev
        prev = cur

    return numinc


if __name__ == "__main__":
    main()
