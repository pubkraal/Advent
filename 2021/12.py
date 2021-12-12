#!/usr/bin/env python3

import sys
from collections import defaultdict

from util.aoc import file_to_day
from util.input import load_data


def main(test=False):
    nodes = defaultdict(list)
    data = load_data(file_to_day(__file__), test)
    for edge in data:
        parent, child = edge.split("-")
        nodes[parent].append(child)
        nodes[child].append(parent)

    print("2021:12:1 =", len(search(nodes, "start", [])))
    print("2021:12:2 =", len(search(nodes, "start", [], True)))


def search(nodes, root, visited, p2=False, little=None):
    paths = []
    visited.append(root)

    for node in nodes[root]:
        if node == "end":
            paths.append([node])
        elif node == "start":
            pass
        elif node != node.lower():
            paths = paths + search(nodes, node, visited.copy(), p2, little)
        else:
            if node in visited:
                if p2 and little is None:
                    paths = paths + search(
                        nodes, node, visited.copy(), p2, node
                    )
            else:
                paths = paths + search(nodes, node, visited.copy(), p2, little)

    retpaths = []
    for path in paths:
        retpaths.append([root] + path)

    return retpaths


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
