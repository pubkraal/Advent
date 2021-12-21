#!/usr/bin/env python3

import sys
from collections import Counter, defaultdict

from util.aoc import file_to_day
from util.input import load_data


class DeterministicDice:
    def __init__(self):
        self.pos = 1
        self.rolls = 0

    def get_rolls(self, num=1):
        rolls = list(range(self.pos, self.pos + num))
        self.pos = rolls[-1] + 1
        while self.pos > 100:
            self.pos -= 100
        self.rolls += len(rolls)
        return [r % 100 if r > 100 else r for r in rolls]

    def how_often(self):
        return self.rolls


def main(test=False):
    data = load_data(file_to_day(__file__), test)

    p1_pos = int(data[0].split()[-1])
    p2_pos = int(data[1].split()[-1])

    p1 = deterministic(p1_pos, p2_pos)
    p2 = all_the_universes(p1_pos, p2_pos)
    print("2021:21:1 =", p1)
    print("2021:21:2 =", p2)


def all_the_universes(p1in, p2in):
    dice = list(
        Counter(
            i + j + k
            for i in range(1, 4)
            for j in range(1, 4)
            for k in range(1, 4)
        ).items()
    )
    universes = {(0, p1in, 0, p2in): 1}
    p1_wins = 0
    p2_wins = 0
    while universes:
        new_universes = defaultdict(int)
        for current_universe, count in list(universes.items()):
            score1, pos1, score2, pos2 = current_universe
            for roll, roll_count in dice:
                p1_pos = (pos1 + roll - 1) % 10 + 1
                p1_score = score1 + p1_pos
                if p1_score >= 21:
                    p1_wins += count * roll_count
                    continue
                for d2, d2count in dice:
                    p2_pos = (pos2 + d2 - 1) % 10 + 1
                    p2_score = score2 + p2_pos
                    if p2_score >= 21:
                        p2_wins += count * roll_count * d2count
                        continue
                    new_universes[(p1_score, p1_pos, p2_score, p2_pos)] += (
                        count * roll_count * d2count
                    )
        universes = new_universes

    return max([p1_wins, p2_wins])


def deterministic(p1in, p2in):
    p1_pos = p1in
    p2_pos = p2in
    p1_score = 0
    p2_score = 0

    d = DeterministicDice()

    i = 0
    while p1_score < 1000 and p2_score < 1000:
        r = d.get_rolls(3)
        if i % 2 == 0:
            p1_pos, p1_score = move(p1_pos, p1_score, r)
        else:
            p2_pos, p2_score = move(p2_pos, p2_score, r)
        i += 1
    return min([p1_score, p2_score]) * d.how_often()


def move(pos, score, rolls):
    pos = pos + sum(rolls)
    while pos > 10:
        pos -= 10
    return pos, (score + pos)


if __name__ == "__main__":
    test = len(sys.argv) > 1 and sys.argv[1] == "test"
    main(test)
