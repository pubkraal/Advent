#!/usr/bin/env python3
import sys
from math import ceil


def main(filename):
    with open(filename, "r") as rd:
        data = rd.readlines()

    num = int(data[0])
    schedule = data[1].strip().split(",")
    service = [int(x) for x in schedule if x != "x"]
    buses = [(int(x), idx) for idx, x in enumerate(schedule) if x != "x"]

    bus = 0
    depart = 0
    for s in service:
        n = ceil(num / s) * s
        if depart == 0 or depart > n:
            depart = n
            bus = s

    print("1: ", (depart - num) * bus)

    p, t = 1, 0
    for bus, idx in buses:
        while True:
            if (idx + t) % bus == 0:
                break
            t += p
        p *= bus
    print("2: ", t)


if __name__ == "__main__":
    main(sys.argv[1])
