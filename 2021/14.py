#!/usr/bin/env python3

import sys
from collections import Counter

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    data = load_data(file_to_day(__file__), test)

    start = data[0]
    poly = Counter([start[b : b + 2] for b in range(len(start) - 1)])
    rules = dict()
    for rule in data[2:]:
        pair, extra = rule.split(" -> ", 1)
        rules[pair] = extra

    for i in range(40):
        poly = inject(poly, rules)
        if i == 9:
            print("2021:14:1 =", calc_score(poly, start))

    print("2021:14:2 =", calc_score(poly, start))


def calc_score(poly, start):
    c = Counter([start[0], start[-1]])
    for key, num in poly.items():
        for letter in key:
            c[letter] += num
    return (c.most_common()[0][1] - c.most_common()[-1][1]) // 2


def inject(poly, rules):
    newpoly = Counter()
    for key, value in poly.items():
        newpoly[key[0] + rules[key]] += value
        newpoly[rules[key] + key[1]] += value
    return newpoly


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
