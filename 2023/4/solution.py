import os
import re
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_numbers(line):
    without_prefix = re.split(': +', line)[1]
    splits = re.split(' +\| +', without_prefix)
    winning_numbers, my_numbers = ([int(n) for n in re.split(' +', split)] for split in splits)
    return np.array(winning_numbers), np.array(my_numbers)


def get_won_numbers(line):
    winning_numbers, my_numbers = get_numbers(line)
    return np.intersect1d(winning_numbers, my_numbers)


def get_points(line):
    won_numbers = get_won_numbers(line)
    return int(pow(2, len(won_numbers) - 1))


points = [get_points(line) for line in lines]
print(np.sum(points))

cards = [1 for i in range(len(lines))]
played_cards = [0 for card in cards]
for card_to_play in range(len(cards)):
    n_won_numbers = len(get_won_numbers(lines[card_to_play]))
    n_cards = cards[card_to_play]
    for i in range(n_won_numbers):
        if card_to_play+i+1 < len(lines):
            cards[card_to_play + i + 1] += n_cards
print(np.sum(cards))
