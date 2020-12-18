#!/usr/bin/env python3
import sys


def main(filename):
    with open(filename) as rd:
        data = rd.readlines()

    t = 0
    t2 = 0
    for line in data:
        t += evaluate(line)
        t2 += evaluate(line, True)

    print("1: ", t)
    print("2: ", t2)


def evaluate(fmath, sep=False):
    newf = fmath
    bracketies = []
    while '(' in newf:
        for i, c in enumerate(newf):
            if c == '(':
                bracketies.append(i)
            elif c == ')':
                o = bracketies.pop()
                sub = newf[o:i+1]
                bracketies.clear()
                newf = newf.replace(sub, str(evaluate(sub[1:-1], sep)))
                break

    res = 0
    steps = newf.split(" ")
    if sep:
        # Now that it's flat, solve + first, then the *. Something with part 2
        for pos, x in [(idx, y) for idx, y in enumerate(steps) if y == '+'][::-1]:  # noqa
            tmp = int(steps[pos-1]) + int(steps[pos+1])
            steps = steps[:pos-1] + [str(tmp)] + steps[pos+2:]
        res = 1
        for x in (int(x) for x in steps if x != '*'):
            res *= x
    else:
        for pos, x in ((idx, y) for idx, y in enumerate(steps)
                       if y in ('+', '*')):
            c = int(steps[pos-1])
            if pos != 1:
                c = res
            if x == '+':
                res = c + int(steps[pos+1])
            elif x == '*':
                res = c * int(steps[pos+1])

    return res


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("nee")
        sys.exit(1)

    assert evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2", True) == 23340  # noqa
    assert evaluate("2 * 3 + (4 * 5)", True) == 46
    assert evaluate("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2") == 13632
    assert evaluate("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))") == 12240
    assert evaluate("5 + (8 * 3 + 9 + 3 * 4 * 3)") == 437
    assert evaluate("2 * 3 + (4 * 5)") == 26

    main(sys.argv[1])
