#!/usr/bin/env python3

from functools import reduce

from util.aoc import file_to_day
from util.input import load_data


def main():
    boards = []
    data = list(load_data(file_to_day(__file__)))

    order = list(map(int, data[0].split(",")))

    for i in range(len(data) // 6):
        boards.append(
            [
                list(map(int, line.strip().split()))
                for line in data[i * 6 + 2 : i * 6 + 7]
            ]
        )

    winners = find_winners(boards, order)

    print("2021:04:1 =", winners[0])
    print("2021:04:2 =", winners[-1])


def find_winners(boards, order):
    use_boards = boards
    winners = []
    for i in range(len(order) - 5):
        called = order[0 : i + 5]

        winning_boards = []
        for j in range(len(use_boards)):
            brd = boards[j]
            winning = check_winner(brd, called)
            if winning:
                winners.append(sum(winning) * called[-1])
                winning_boards.append(j)
        for j in winning_boards[::-1]:
            use_boards.pop(j)

    return winners


def check_winner(board, picked):
    # build rows of columns
    rows = [set(r) for r in board]
    rows += [set(c) for c in zip(*board)]

    pick = set(picked)
    for r in rows:
        if (r & pick) == r:
            boardset = set(reduce(lambda a, b: a + b, board))
            unmarked = boardset - pick
            return unmarked
    return []


if __name__ == "__main__":
    main()
