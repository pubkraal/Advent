#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    fish = Counter(
        int(f)
        for f in load_data(file_to_day(__file__), test)[0].strip().split(",")
    )

    part1 = generate(fish, 80)

    print("2021:06:1 =", sum(part1.values()))
    print("2021:06:2 =", sum(generate(part1, generations=256 - 80).values()))


def generate(fish, generations):
    for _ in range(generations):
        newfish = defaultdict(int)
        for age, number in fish.items():
            if age <= 0:
                newfish[6] += number
                newfish[8] += number
            else:
                newfish[age - 1] += number
        fish = newfish
    return fish


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
