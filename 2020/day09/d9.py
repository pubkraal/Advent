#!/usr/bin/env python3
import itertools
import sys

with open("input.txt", "r") as rd:
    data = [int(x) for x in rd.readlines()]


for offset, x in enumerate(data[25:]):
    d = [y[0] + y[1] for y in itertools.combinations(data[offset:offset+25], 2)]
    if x not in d:
        print("1: ", x)
        for y in range(2, 1000):
            for z in range(0, len(data) - y):
                d2 = data[z:z+y]
                t = sum(d2)
                if t == x:
                    print("2: ", min(d2) + max(d2))
                    sys.exit(0)
