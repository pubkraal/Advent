#!/usr/bin/env python3
from functools import reduce


def solve1(in_):
    prev = in_
    while True:
        new = apply(prev)
        if new == prev:
            break
        prev = new
    print("1: ", sum(1 for x in reduce(lambda a,b: a+b, prev) if x == '#'))

def apply(in_):
    """
    If a seat is empty (L) and there are no occupied seats adjacent to it, the
    seat becomes occupied.
    If a seat is occupied (#) and four or more seats adjacent to it are also
    occupied, the seat becomes empty.
    Otherwise, the seat's state does not change.
    """
    newmap = []
    for y, l in enumerate(in_):
        newl = []
        for x, p in enumerate(l):
            val = p
            adj = adjseats(x, y, in_)
            if val == "L":
                if not any(x == '#' for x in adj):
                    val = "#"
            elif val == "#":
                if sum(1 for x in adj if x == "#") >= 4:
                    val = "L"

            newl.append(val)
        newmap.append(newl)

    return newmap


# This could be useful if I wanted to make a graphical output
def m2s(in_):
    return "\n".join(''.join(l) for l in in_)


def adjseats(x, y, map_):
    x_min = max(0, x-1)
    x_max = min(len(map_[0])-1, x+1)
    y_min = max(0, y-1)
    y_max = min(len(map_)-1, y+1)

    seats = []
    for rx in range(x_min, x_max+1):
        for ry in range(y_min, y_max+1):
            if [rx, ry] == [x, y]:
                continue
            seats.append(map_[ry][rx])
    return seats

def solve2(in_):
    prev = in_
    while True:
        new = apply2(prev)
        if new == prev:
            break
        prev = new
    print("2: ", sum(1 for x in reduce(lambda a,b: a+b, prev) if x == "#"))

def apply2(in_):
    newmap = []
    for y, l in enumerate(in_):
        newl = []
        for x, p in enumerate(l):
            val = p
            newl.append(val)
        newmap.append(newl)
    return newmap

def find_first(map_, x, y):
    xmax = len(map_[0])-1
    ymax = len(map_)-1

    return map_[y][x]

if __name__ == "__main__":
    with open("input.txt", "r") as rd:
        data = [list(x.strip()) for x in rd.readlines()]
    solve1(data)
    solve2(data)

