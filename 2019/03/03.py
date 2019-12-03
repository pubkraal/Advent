#!/usr/bin/env python3
import sys


def parse_path(path):
    return []


def trace_path(map_, path):
    return []


def find_distance(paths):
    # trace paths
    map_ = {}
    parsed_paths = [parse_path(path) for path in paths]
    for path in parsed_paths:
        crossings = trace_path(map_, path)

    return 0


def main(inputfile):
    assert find_distance(["R8,U5,L5,D3", "U7,R6,D4,L4"]) == 3
    assert find_distance(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 159
    assert find_distance(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 135


if __name__ == "__main__":
    main(sys.argv[1])
