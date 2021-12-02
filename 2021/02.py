#!/usr/bin/env python3

from util.aoc import file_to_day
from util.input import load_data


def main():
    aim = 0
    x, y, y2 = 0, 0, 0

    for line in load_data(file_to_day(__file__)):
        dir, num = line.split()
        num = int(num)
        mx, my, ma, mv = {
            "forward": (1, 0, 0, 1),
            "back": (-1, 0, 0, 0),
            "down": (0, 1, 1, 0),
            "up": (0, -1, -1, 0),
        }[dir]

        x += num * mx
        y += num * my
        aim += num * ma
        y2 += (num * mv) * aim

    print("2021:02:1 =", x * y)
    print("2021:02:2 =", x * y2)


if __name__ == "__main__":
    main()
