#!/usr/bin/env python3
import sys
from itertools import product

ADD = 1
MUL = 2
TRM = 99


def set_position(program, position, value):
    if position > len(program) - 1:
        # Protection against out of bounds
        # Append zeroes until position met
        program += [0] * (position - (len(program) - 1))
    program[position] = value
    return program


def execute_program(program):
    pos = 0
    while True:
        if pos > len(program) - 1:
            print("Panic!")
            break
        instruction = program[pos]
        if instruction == ADD:
            res = program[program[pos+1]] + program[program[pos+2]]
            program = set_position(program, program[pos+3], res)
            pos += 4
        elif instruction == MUL:
            res = program[program[pos+1]] * program[program[pos+2]]
            program = set_position(program, program[pos+3], res)
            pos += 4
        elif instruction == TRM:
            break

    return program


def parse_program(program):
    return [int(x) for x in program.split(',')]


def main(inputfile):
    assert execute_program([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert execute_program([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert execute_program([2, 4, 4, 5, 99]) == [2, 4, 4, 5, 99, 9801]
    assert execute_program([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

    program = []
    with open(inputfile, 'r') as rd:
        program = parse_program(rd.read())

    orig = program[::]
    result = execute_program(program)
    print("Challenge one:", result[0])

    # Find combination that yields 19690720
    for idx, comb in enumerate(product(range(100), repeat=2)):
        try_prog = orig[::]
        try_prog[1] = comb[0]
        try_prog[2] = comb[1]
        result = execute_program(try_prog)
        if result[0] == 19690720:
            print("Challenge two:", 100 * comb[0] + comb[1])
            break
    else:
        print("Challenge two: Failed")


if __name__ == "__main__":
    main(sys.argv[1])
