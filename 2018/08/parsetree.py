#!/usr/bin/env python3
import sys
from functools import reduce


class Node:
    def __init__(self, child_nodes=0, metadata=0):
        self.num_nodes = child_nodes
        self.num_metadata = metadata
        self.child_nodes = []
        self.metadata = []

    def add_node(self, node):
        self.child_nodes.add(node)

    def add_nodes(self, nodes):
        self.child_nodes += nodes

    def add_metadata(self, data):
        self.metadata.add(data)

    def add_metadatas(self, datas):
        self.metadata += datas


def parse_tree(data, nodes, expect_nodes=1):
    # Nodes are:
    # Number of childnodes
    # Number of metadata
    # <Childnodes>
    # <metadata>
    # So we go recursive, woop.
    # We parse every node at this level and return a list

    metadata = data[1]
    childnodes = data[0]

    print(metadata, childnodes)
    n = Node(childnodes, metadata)
    nodes.append(n)
    moved = 0

    if childnodes > 0:
        cnodes, cursor_moved = parse_tree(data[2:], nodes, childnodes)
        start = cursor_moved + 2
        n.add_nodes(cnodes)
        n.add_metadatas(data[start:start + metadata])
        moved = start + metadata
    else:
        n.add_metadatas(data[2:2 + metadata])
        moved = 2 + metadata

    return [n, moved]


def main(inputfile):
    nodes = []
    with open(inputfile, 'r') as rd:
        data = list(map(int, rd.read().split()))
    rootnodes = parse_tree(data, nodes)

    print(rootnodes)
    print("Total sum:", sum(reduce(lambda a, b: a+b,
                                   [n.metadata for n in nodes])))


if __name__ == "__main__":
    main(sys.argv[1])
