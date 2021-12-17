#!/usr/bin/env python3

import sys
import re
from itertools import product

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    data = load_data(file_to_day(__file__), test)[0]
    r = re.compile(r"((-?[\d]+)..(-?[\d]+))")
    m = r.findall(data)
    sx, ex, sy, ey = tuple(
        int(x) for x in (m[0][1], m[0][2], m[1][1], m[1][2])
    )

    vectors = product(range(ex + 1), range(sy, abs(sy) + 1))
    max_y = 0
    ok = set()

    for x, y in vectors:
        px, py = 0, 0
        ys = [py]
        vx, vy = x, y
        while px <= ex and py >= sy:
            px += vx
            py += vy
            ys.append(py)

            if sx <= px <= ex and sy <= py <= ey:
                ok.add((x, y))
                max_y = max(max_y, *ys)
                break

            vx = max(0, vx - 1)
            vy -= 1

    print("2021:17:1 =", max_y)
    print("2021:17:2 =", len(ok))


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
