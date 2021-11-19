#!/usr/bin/env python3

def main():
    calc = dict()
    results = dict()

    with open("../input/07.txt") as rd:
        for line in rd.readlines():
            (ops, res) = line.split("->")
            calc[res.strip()] = ops.strip().split()

    def calculate(name, override):
        try:
            return int(name)
        except:
            pass

        if name not in results:
            ops = calc[name]
            if override is not None and name in override:
                res = override[name]
            elif len(ops) == 1:
                res = calculate(ops[0], override)
            else:
                op = ops[-2]
                if op == "AND":
                    res = calculate(ops[0], override) & calculate(ops[2], override)
                elif op == "OR":
                    res = calculate(ops[0], override) | calculate(ops[2], override)
                elif op == "NOT":
                    res = ~calculate(ops[1], override) & 0xffff
                elif op == "RSHIFT":
                    res = calculate(ops[0], override) >> calculate(ops[2], override)
                elif op == "LSHIFT":
                    res = calculate(ops[0], override) << calculate(ops[2], override)

            results[name] = res

        return results[name]
    aval = calculate("a", dict())
    print("part 1: %d" % aval)
    results = dict()
    print("part 2: %d" % calculate("a", {"b": aval}))

if __name__ == "__main__":
    main()