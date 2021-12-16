#!/usr/bin/env python3

import sys

# from util.aoc import file_to_day
# from util.input import load_data

# Packet structure is
# VVVTTT
# 0000111122223333...
# V = Version
# T = Type.
#     4 = 15 bits of data, discard 0, 5, 10
#    !4 = followed by I on pos 6 (hex 2)
# I = Length Type ID
#     0 = 15 bit L + L = bits of numbers
#     1 = 11 bit L + L = number of 11bit packets
#
# VVVTTTILLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBCCCCCCCCCCC.....
# VVVTTTILLLLLLLLLLLLLLLAAAAAAAAAAABBBBBBBBBBBBBBBB.......
# 00001111222233334444555566667777888899990000111122223333
# 00111000000000000110111101000101001010010001001000000000


def main(test=False):
    # data = load_data(file_to_day(__file__), test)
    # instructions = "{:b}".format(int(data[0], 16))

    print("go version only")


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
