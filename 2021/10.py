#!/usr/bin/env python3

import sys

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    data = load_data(file_to_day(__file__), test)
    print(data)


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
