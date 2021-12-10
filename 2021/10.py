#!/usr/bin/env python3

import sys
from statistics import median

from util.aoc import file_to_day
from util.input import load_data

OPEN = ("(", "[", "{", "<")
CLOSE = (")", "]", "}", ">")
POINTS = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
COMPLPOINTS = {
    "(": 1,
    "[": 2,
    "{": 3,
    "<": 4,
}


def main(test=False):
    p1 = 0
    p2 = []

    for line in (x.strip() for x in load_data(file_to_day(__file__), test)):
        stack = []
        for c in line:
            if c in OPEN:
                stack.append(c)
            else:
                o = stack.pop()
                s = CLOSE[OPEN.index(o)]
                if s != c:
                    p1 += POINTS[c]
                    break
        else:
            p = 0
            for item in stack[::-1]:
                p *= 5
                p += COMPLPOINTS[item]
            p2.append(p)

    print("2021:10:1 =", p1)
    print("2021:10:2 =", median(sorted(p2)))


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
