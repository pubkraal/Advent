#!/usr/bin/env python3
import sys


def main(filename):
    with open(filename) as rd:
        data = [int(x) for x in rd.readlines()[0].split(",")]

    spoken = data
    last = {v: k for k, v in enumerate(spoken)}
    for x in range(len(data), 30000000):
        if spoken[-1] in last:
            spoken.append(x - last[spoken[-1]] - 1)
        else:
            spoken.append(0)
        last[spoken[-2]] = x-1
        if len(spoken) == 2020:
            print("1: ", spoken[-1])
    print("2: ", spoken[-1])


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("NEED INPUT")
        sys.exit(1)
    main(sys.argv[1])
