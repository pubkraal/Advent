#!/usr/bin/env python3

from util.aoc import file_to_day
from util.input import load_data


def main():
    aim = 0
    x, y = 0, 0
    x2, y2 = 0, 0

    for line in load_data(file_to_day(__file__)):
        dir, num = line.split()
        num = int(num)
        if dir == "forward":
            x += num
            x2 += num
            y2 += aim * num
        elif dir == "back":
            x -= num
            x2 -= num
        if dir == "down":
            y += num
            aim += num
        elif dir == "up":
            y -= num
            aim -= num

    print("2021:02:1 =", x * y)
    print("2021:02:2 =", x2 * y2)


if __name__ == "__main__":
    main()
