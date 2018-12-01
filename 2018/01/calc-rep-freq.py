#!/usr/bin/env python3
import sys


def main(inputfile):
    with open(inputfile, 'r') as rd:
        print("Resulting frequency:", find_rep_freq(0, rd))


def find_rep_freq(start, rd):
    current = start
    counter = 0
    mutations = [int(x.strip()) for x in rd.readlines()]
    max_mut = len(mutations)
    found_freqs = set()
    while True:
        mut = mutations[counter % max_mut]
        counter += 1
        current += mut
        if current in found_freqs:
            break
        found_freqs.add(current)
    return current


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
