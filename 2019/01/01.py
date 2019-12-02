#!/usr/bin/env python3
import sys


def fuel_need(num):
    return max(0, int(num / 3) - 2)


def reduced_fuel_need(num):
    step = num
    total = 0
    for x in range(100):
        more_fuel = fuel_need(step)
        if more_fuel == 0:
            break

        total += more_fuel
        step = more_fuel

    return total


def main(input_file):
    assert fuel_need(12) == 2
    assert fuel_need(14) == 2
    assert fuel_need(1969) == 654
    assert fuel_need(100756) == 33583

    all_fuels = []

    with open(input_file, 'r') as rd:
        for line in rd.readlines():
            num = int(line)
            fuel = fuel_need(num)
            all_fuels.append(fuel)

    print("Fuel need:", sum(all_fuels))

    additional_fuels = [reduced_fuel_need(x) for x in all_fuels]

    print("Fuel need w/ fuel:", sum(all_fuels) + sum(additional_fuels))


if __name__ == "__main__":
    main(sys.argv[1])
