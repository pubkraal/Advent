#!/usr/bin/env python3
import os
import sys


def is_valid(num, verbose=False):
    if len(num) > 6:
        return False

    has_doubles = False
    prev = ""
    for x in num:
        if not prev:
            prev = x
            continue
        if int(x) < int(prev):
            return False
        if x == prev:
            has_doubles = True
        prev = x
    return has_doubles


def main(inputfile):
    if not os.getenv("SKIPASSERT"):
        assert is_valid("111111") == True
        assert is_valid("223450") == False
        assert is_valid("123789") == False
        assert is_valid("699968", True) == False

    with open(inputfile) as rd:
        range_ = range(*[int(r) for r in rd.read().split("-", 2)])
        valid = [num for num in range_ if is_valid(str(num))]
        print(valid)
        print("One:", len(valid))


if __name__ == "__main__":
    main(sys.argv[1])

