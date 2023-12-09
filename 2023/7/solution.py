import itertools
import os
import sys

import pandas as pd

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_hand_and_bid(line):
    parts = line.split(' ')
    return parts[0], int(parts[1])


def get_card_value(card, new_version):
    if new_version:
        if card == 'J':
            return 0
        elif card.isdigit():
            return int(card) - 1
        elif card == 'T':
            return 9
        elif card == 'Q':
            return 10
        elif card == 'K':
            return 11
        elif card == 'A':
            return 12
        else:
            raise ValueError()

    if card.isdigit():
        return int(card) - 2
    elif card == 'T':
        return 8
    elif card == 'J':
        return 9
    elif card == 'Q':
        return 10
    elif card == 'K':
        return 11
    elif card == 'A':
        return 12
    else:
        raise ValueError()


def get_type(hand, new_version):
    cards = [get_card_value(card, new_version) for card in hand]
    groups = []
    jokers = 0
    for k, g in itertools.groupby(sorted(cards)):
        if new_version and k == 0:  # Joker
            jokers += len(list(g))
        else:
            groups.append((len(list(g)), k))
    groups = sorted(groups, key=lambda g: g[0], reverse=True)
    if jokers == 5:
        return 6
    groups[0] = (groups[0][0] + jokers, groups[0][1])

    if len(groups) == 1:
        return 6  # Five of a kind
    elif len(groups) == 2 and groups[0][0] == 4:
        return 5  # Four of a kind
    elif len(groups) == 2:
        return 4  # Full house
    elif groups[0][0] == 3:
        return 3  # Three of a kind
    elif len(groups) == 3:
        return 2  # Two pairs
    elif len(groups) == 4:
        return 1  # One pair
    else:
        return 0


def get_valuation(hand, new_version):
    card_values = [get_card_value(card, new_version) for card in hand]
    filled = [str(val).zfill(2) for val in card_values]
    concatenated = "".join(filled)
    return int(concatenated)


data = pd.DataFrame(lines, columns=['line'])
data['hand'] = [get_hand_and_bid(line)[0] for line in lines]
data['bid'] = [get_hand_and_bid(line)[1] for line in lines]
data['type'] = data['hand'].apply(get_type, new_version=False)
data['valuation'] = data['hand'].apply(get_valuation, new_version=False)
data = data.sort_values(['type', 'valuation'], ignore_index=True)
data['rank'] = data.index + 1
data['winnings'] = data['bid'] * data['rank']

print(sum(data['winnings']))

data['new_type'] = data['hand'].apply(get_type, new_version=True)
data['new_valuation'] = data['hand'].apply(get_valuation, new_version=True)
data = data.sort_values(['new_type', 'new_valuation'], ignore_index=True)
data['new_rank'] = data.index + 1
data['new_winnings'] = data['bid'] * data['new_rank']

print(sum(data['new_winnings']))


