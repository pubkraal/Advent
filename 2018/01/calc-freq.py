#!/usr/bin/env python3
import sys


def main(inputfile):
    with open(inputfile, 'r') as rd:
        print("Resulting frequency:", calculate_freq(0, rd))


def calculate_freq(start, rd):
    mutations = [int(x.strip()) for x in rd.readlines()]
    for mut in mutations:
        start += mut
    return start


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: %s inputfile", sys.argv[0])
        sys.exit(0)
    main(sys.argv[1])
