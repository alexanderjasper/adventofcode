import os
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_game_rgbs(line):
    handfuls = line.split(': ')[1].split('; ')
    rgbs = []
    for handful in handfuls:
        color_draws = handful.split(', ')
        rgb = [0, 0, 0]
        for color_draw in color_draws:
            amount, color = color_draw.split(' ')
            amount = int(amount)
            match color:
                case 'red':
                    rgb[0] = amount
                case 'green':
                    rgb[1] = amount
                case 'blue':
                    rgb[2] = amount
        rgbs.append(rgb)
    return rgbs


def is_possible(rgbs, max_rgb):
    return all((np.max(rgbs, axis=0) <= max_rgb))


sum_ids = 0
for line in lines:
    game_id = int(line.split(':')[0][5:])
    rgbs = get_game_rgbs(line)
    if is_possible(rgbs, [12, 13, 14]):
        sum_ids += game_id
print(sum_ids)


def get_fewest_feasible(rgbs):
    return np.max(rgbs, axis=0)


def get_power(rgb):
    return np.prod(rgb)


sum_power = 0
for line in lines:
    rgbs = get_game_rgbs(line)
    fewest_feasible = get_fewest_feasible(rgbs)
    power = get_power(fewest_feasible)
    sum_power += power
print(sum_power)
