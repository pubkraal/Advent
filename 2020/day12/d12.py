#!/usr/bin/env python3
import sys


def main(filename):
    with open(filename, "r") as rd:
        data = [(l[0], int(l[1:].strip())) for l in rd.readlines()]

    wayp = [10, -1]
    pos = [0,0]
    pos2 = [0,0]
    vector = 90

    vs = {0: (0, -1),
          180: (0, 1),
          90: (1, 0),
          270: (-1, 0)}
    dirs = {"N": (0, -1),
            "S": (0, 1),
            "E": (1, 0),
            "W": (-1, 0)}

    for idx, n in enumerate(data):
        v = n[0]
        if v == "L":
            vector = (vector - n[1]) % 360

            for x in range(n[1] // 90):
                newx = wayp[1]
                newy = -wayp[0]
                wayp = [newx, newy]
        elif v == "R":
            vector = (vector + n[1]) % 360

            for x in range(n[1] // 90):
                newx = -wayp[1]
                newy = wayp[0]
                wayp = [newx, newy]
        elif v == "F":
            d = vs[vector]
            pos[0] += d[0]*n[1]
            pos[1] += d[1]*n[1]

            pos2[0] += wayp[0] * n[1]
            pos2[1] += wayp[1] * n[1]
        else:
            d = dirs[n[0]]
            pos[0] += d[0]*n[1]
            pos[1] += d[1]*n[1]

            wayp[0] += d[0]*n[1]
            wayp[1] += d[1]*n[1]
        print("%03d" % (idx,), n, wayp, pos2)

    print("1: ", abs(pos[0]) + abs(pos[1]))
    print("2: ", abs(pos2[0]) + abs(pos2[1]))


if __name__ == "__main__":
    main(sys.argv[1])
