#!/usr/bin/env python3

import sys
import json

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    numbers = [
        json.loads(line) for line in load_data(file_to_day(__file__), test)
    ]

    p1_res = numbers[0]
    for num in numbers[1:]:
        p1_res = add(p1_res, num)

    p2 = 0
    for num in numbers:
        for num2 in numbers:
            if num != num2:
                p2 = max(p2, magnitude(add(num, num2)))

    print("2021:18:1 =", magnitude(p1_res))
    print("2021:18:2 =", p2)


def add(n1, n2):
    return reduce([n1, n2])


def reduce(n):
    d1, n1 = explode(n)
    if d1:
        return reduce(n1)

    d2, n2 = split(n)
    if d2:
        return reduce(n2)
    return n2


def split(n):
    if isinstance(n, list):
        did1, n1 = split(n[0])
        if did1:
            return True, [n1, n[1]]
        did2, n2 = split(n[1])
        return did2, [n1, n2]

    if n >= 10:
        return True, [n // 2, (n + 1) // 2]
    return False, n


def explode(n):
    ns = str(n)
    parts = []
    i = 0
    while i < len(ns):
        if ns[i] in "[,]":
            parts.append(ns[i])
            i += 1
        elif ns[i] == " ":
            i += 1
        else:
            j = i
            while j < len(ns) and ns[j].isdigit():
                j += 1
            parts.append(int(ns[i:j]))
            i = j

    depth = 0
    for i, c in enumerate(parts):
        if c == "[":
            depth += 1
            if depth <= 4:
                continue

            left = parts[i + 1]
            right = parts[i + 3]
            left_i = None
            right_i = None
            for j in range(len(parts)):
                if isinstance(parts[j], int) and j < i:
                    left_i = j
                elif (
                    isinstance(parts[j], int) and j > i + 3 and right_i is None
                ):
                    right_i = j
            if right_i is not None:
                parts[right_i] += right
            parts = parts[:i] + [0] + parts[i + 5 :]
            if left_i is not None:
                parts[left_i] += left
            return True, json.loads("".join([str(p) for p in parts]))
        elif c == "]":
            depth -= 1
    return False, n


def magnitude(n):
    if isinstance(n, list):
        return 3 * magnitude(n[0]) + 2 * magnitude(n[1])
    return n


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
