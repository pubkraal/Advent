#!/usr/bin/env python3
import sys
from functools import lru_cache
from itertools import combinations


def main(filename):
    with open(filename) as rd:
        data = [x.strip() for x in rd.readlines()]

    mem = dict()
    mem2 = dict()
    mask = ""
    for l in data:
        loc, val = l.split(" = ")
        if loc == "mask":
            mask = val
        else:
            addr = int(loc.replace("mem[", "").replace("]", ""))
            mem[addr] = apply_mask(mask, int(val))
            p2addrs = get_addresses(mask, addr)
            for addr2 in p2addrs:
                mem2[addr2] = int(val)

    print("1: ", sum(mem.values()))
    print("2: ", sum(mem2.values()))


def apply_mask(mask, value):
    brep = "{:b}".format(value)
    newval = list(mask.replace("X", "0"))
    for i, x in enumerate(brep[::-1]):
        mv = mask[-(i+1)]
        if mv == "X":
            newval[-(i+1)] = brep[-(i+1)]

    return int(''.join(newval), 2)


def get_addresses(mask, addr):
    cnt = sum(1 for x in mask if x == 'X')
    t = make_combis(cnt)
    maskval = int(mask.replace("X", "0"), 2)
    base = addr | maskval

    addrs = set()
    for s in t:
        done = 0
        newaddr = list("{:036b}".format(base))
        for i, c in enumerate(mask):
            if c == "X":
                newaddr[i] = str(s[done])
                done += 1
        addrs.add(int(''.join(newaddr), 2))

    return addrs


@lru_cache(maxsize=None)
def make_combis(num):
    return list(set(combinations([0, 1] * num, num)))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("INPUT!")
        sys.exit(1)
    main(sys.argv[1])
