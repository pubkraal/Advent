#!/usr/bin/env python3
import re
import sys


def main(filename):
    with open(filename) as rd:
        raw, mine, near = rd.read().split("\n\n")

    my_ticket = [int(x) for x in mine.splitlines()[-1].split(",")]
    nearby = [[int(y) for y in x.split(",")] for x in near.splitlines()[1:]]
    parsed = re.findall(r'(.+): (\d+)-(\d+) or (\d+)-(\d+)', raw)
    rules = {name: rule(ranges) for name, *ranges in parsed}

    invalid = 0
    valid_tickets = [my_ticket]
    for t in nearby:
        i = invalid_nums(t, rules)
        if i is None:
            valid_tickets.append(t)
        else:
            invalid += i
    print("1: ", invalid)

    matches = {name: get_match(rule, valid_tickets)
               for name, rule in rules.items()}
    previous = set()
    s2 = 1
    for name, cols in sorted(matches.items(), key=lambda x: len(x[1])):
        if name.startswith("departure"):
            s2 *= my_ticket[next(iter(cols - previous))]
        previous = cols
    print("2: ", s2)


def invalid_nums(t, rules):
    for v in t:
        if not any(rule(v) for rule in rules.values()):
            return v
    return None


def rule(line):
    m1, n1, m2, n2 = map(int, line)

    def r(n):
        return m1 <= n <= n1 or m2 <= n <= n2
    return r


def get_match(rule, valid_tickets):
    return set.intersection(
        *({idx for idx, value in enumerate(valid) if rule(value)}
          for valid in valid_tickets)
    )


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("ASJDKHSADL:FSD")
        sys.exit(1)
    main(sys.argv[1])
