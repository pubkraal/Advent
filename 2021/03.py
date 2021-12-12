#!/usr/bin/env python3

from util.aoc import file_to_day
from util.input import load_data


def main():
    bits = list(load_data(file_to_day(__file__)))
    numlines = len(bits)

    reg = build_reg(bits)
    compute = [0] * 12

    # Part 1
    for idx, char in enumerate(reg):
        compute[idx] = int(char / numlines >= 0.5)

    gamma = int("".join(map(str, compute)), 2)
    epsilon = gamma ^ 0b111111111111
    print("2021:03:1 =", gamma * epsilon)

    # part 2
    oxy = bits[:]
    co2 = bits[:]
    oxyreg = reg[:]
    co2reg = reg[:]
    oxyres = []
    co2res = []

    for idx in range(12):
        oxyres.append(int(oxyreg[idx] / len(oxy) >= 0.5))
        prefix = "".join(map(str, oxyres))
        oxy = filter_bits(bits, prefix)
        oxyreg = build_reg(oxy)

    for idx in range(12):
        co2res.append(int(co2reg[idx] / len(co2) < 0.5))
        prefix = "".join(map(str, co2res))
        co2 = filter_bits(bits, prefix)
        if len(co2) == 1:
            co2res = co2[0].strip()
            break
        co2reg = build_reg(co2)

    oxyp = int("".join(map(str, oxyres)), 2)
    co2p = int("".join(map(str, co2res)), 2)
    print("2021:03:2 =", oxyp * co2p)


def build_reg(bits):
    reg = [0] * 12
    for line in bits:
        for idx, c in enumerate(line.strip()):
            reg[idx] += int(c)
    return reg


def filter_bits(bits, prefix):
    reg = []
    for line in bits:
        if not line.startswith(prefix):
            continue
        reg.append(line)
    return reg


if __name__ == "__main__":
    main()
