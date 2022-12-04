import os
import sys
import numpy as np
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()


def get_round(input_line):
    return np.array([input_line[:1], input_line[2:3]])


rounds = np.array([get_round(line) for line in lines])


def get_score(opponent, me):
    if (opponent == 'A' and me == 'B' or
        opponent == 'B' and me == 'C' or
            opponent == 'C' and me == 'A'):
        points = 6
    elif (opponent == 'A' and me == 'A' or
          opponent == 'B' and me == 'B' or
          opponent == 'C' and me == 'C'):
        points = 3
    else:
        points = 0

    if (me == 'A'):
        points += 1
    elif (me == 'B'):
        points += 2
    else:
        points += 3
    return points


def get_round_score(round):
    opponent = round[0]
    if round[1] == 'X':
        me = 'A'
    elif round[1] == 'Y':
        me = 'B'
    else:
        me = 'C'

    return get_score(opponent, me)


scores = np.array([get_round_score(round) for round in rounds])

total = np.sum(scores)

print(total)

def get_round_score_ver2(round):
    opponent = round[0]
    strategy = round[1]
    if opponent == 'A':
        if strategy == 'X':
            me = 'C'
        elif strategy == 'Y':
            me = 'A'
        else:
            me = 'B'
    elif opponent == 'B':
        if strategy == 'X':
            me = 'A'
        elif strategy == 'Y':
            me = 'B'
        else:
            me = 'C'
    elif opponent == 'C':
        if strategy == 'X':
            me = 'B'
        elif strategy == 'Y':
            me = 'C'
        else:
            me = 'A'
    return get_score(opponent,me)

scores_ver2 = np.array([get_round_score_ver2(round) for round in rounds])

total_ver2 = np.sum(scores_ver2)

print(total_ver2)