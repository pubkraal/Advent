#!/usr/bin/env python3
from collections import defaultdict


def main(filename):
    with open(filename, "r") as rd:
        d = rd.read().strip()

    housemap = defaultdict(int)

    mutations = {
            "<": (-1, 0),
            ">": (1, 0),
            "^": (0, -1),
            "v": (0, 1),
            }

    x, y = 0,0
    housemap[x,y] += 1
    for i in d:
        mut = mutations[i]
        x += mut[0]
        y += mut[1]
        housemap[x,y] += 1

    print("Step 1:", len(housemap))

    housemap2 = defaultdict(int)
    x, y = 0, 0
    rx, ry = 0, 0
    for idx, i in enumerate(d):
        mut = mutations[i]
        if idx % 2 == 0:
            x += mut[0]
            y += mut[1]
            housemap2[x,y] += 1
        else:
            rx += mut[0]
            ry += mut[1]
            housemap2[rx,ry] += 1

    print("Step 2:", len(housemap2))


if __name__ == "__main__":
    main("input.txt")
