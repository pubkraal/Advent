#!/usr/bin/env python3

from util.aoc import file_to_day
from util.input import load_data


def main():
    n = list(map(int, load_data(file_to_day(__file__))))
    sums = [sum(x) for x in zip(n, n[1:], n[2:])]

    print("2021:01:1 =", get_incs(n))
    print("2021:01:2 =", get_incs(sums))


def get_incs(iter):
    numinc = 0
    prev = float("inf")

    for cur in iter:
        numinc += cur > prev
        prev = cur

    return numinc


if __name__ == "__main__":
    main()
