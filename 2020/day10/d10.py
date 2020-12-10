#!/usr/bin/env python3
from collections import defaultdict
from functools import lru_cache

with open("input.txt", "r") as rd:
    d = sorted([int(x) for x in rd.readlines()])

d.insert(0, 0)
d.append(d[-1] + 3)

steps = defaultdict(int)
prev = 0
for num in d[1:]:
    steps[num - prev] += 1
    prev = num

print("1: ", steps[1] * steps[3])

@lru_cache(maxsize=None)
def ways(adapters):
    if len(adapters) <= 2:
        return 1

    first, rem = adapters[0], adapters[1:]
    return sum(
        ways(r)
        for r
        in map(lambda n: rem[n:], range(len(rem)))
        if r[0] - 3 <= first
    )

print("2: ", ways(tuple(d)))
