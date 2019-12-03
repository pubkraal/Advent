#!/usr/bin/env python3
import os
import sys


def parse_path(path):
    return path.split(",")


def trace_path(path):
    map_ = {}
    pos = (0,0)
    length = 0
    for dir_ in path:
        steps = int(dir_[1:])
        mutation = {
            "L": (-1, 0),
            "U": (0, 1),
            "R": (1, 0),
            "D": (0, -1)
        }[dir_[0]]

        for x in range(steps):
            pos = (pos[0] + mutation[0], pos[1] + mutation[1])
            length += 1
            if pos not in map_:
                map_[pos] = length
    return map_


def calc_distance(dest):
    return abs(dest[0]) + abs(dest[1])


def find_distance(paths):
    # trace paths
    parsed_paths = [parse_path(path) for path in paths]
    map1 = trace_path(parsed_paths[0])
    map2 = trace_path(parsed_paths[1])

    crossings = set(map1.keys()) & set(map2.keys())

    return min([calc_distance(crx) for crx in crossings])


def find_earliest(paths):
    # trace paths
    parsed_paths = [parse_path(path) for path in paths]
    map1 = trace_path(parsed_paths[0])
    map2 = trace_path(parsed_paths[1])

    crossings = set(map1.keys()) & set(map2.keys())

    return min([map1[c] + map2[c] for c in crossings])


def main(inputfile):
    if not os.getenv("SKIPASSERT"):
        assert find_distance(["R8,U5,L5,D3", "U7,R6,D4,L4"]) == 6
        assert find_distance(["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"]) == 159
        assert find_distance(["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"]) == 135

    with open(inputfile) as rd:
        paths = [x.strip() for x in rd.readlines()]
        print("One:", find_distance(paths))
        print("Two:", find_earliest(paths))


if __name__ == "__main__":
    main(sys.argv[1])
