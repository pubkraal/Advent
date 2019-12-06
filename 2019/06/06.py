#!/usr/bin/env python3
import os
import sys
from collections import defaultdict

# Slow way: determine parents for every node
# Fast way: determine children going down and reduce the total score
# I'm taking the slow way
def get_orbits_for_node(tree, node):
    return 1


class Body:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    def set_parent(self, parent):
        self.parent = parent

    def add_child(self, child):
        self.children.append(child)

    def get_sub_orbits(self, steps_from_root=0):
        orbits = steps_from_root
        for child in self.children:
            orbits += child.get_sub_orbits(steps_from_root + 1)
        print("Orbits for", self.name, "are:", orbits)
        return orbits

    def get_sup_orbits(self):
        return 1

    def get_path_to_root(self):
        path = [self.name]
        if self.parent:
            path += self.parent.get_path_to_root()
        return path


def main(inputfile):

    nodes = {}

    with open(inputfile) as rd:
        data = [x.strip().split(')') for x in rd.readlines()]

        for rel in data:
            parent = nodes.get(rel[0], None)
            if not parent:
                parent = Body(rel[0], None)
                nodes[rel[0]] = parent
            child = nodes.get(rel[1], None)
            if not child:
                child = Body(rel[1], parent)
                parent.add_child(child)
                nodes[rel[1]] = child
            else:
                parent.add_child(child)
                child.set_parent(parent)

    # find root
    root = None
    curnode = list(nodes.values())[0]
    for x in range(len(nodes)):
        if not curnode.parent:
            root = curnode
            break
        curnode = curnode.parent
    else:
        print("Infinite loop in orbits, this is cray")
        os.exit(1)

    print("One:", root.get_sub_orbits())
    youp = nodes["YOU"].get_path_to_root()[::-1]
    sanp = nodes["SAN"].get_path_to_root()[::-1]

    # Find last matching node, add lists together, len(), -3. I did it manually

    print("Two-a:", youp)
    print("Two-b:", sanp)
    print("Two:", 0)


if __name__ == "__main__":
    main(sys.argv[1])
