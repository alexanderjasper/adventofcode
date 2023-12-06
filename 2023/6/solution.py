import os
import re
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    puzzle_input = f.read().splitlines()


def get_data(lines, version):
    if version == 1:
        time = [int(s) for s in re.split(' +', lines[0])[1:]]
        distance = [int(s) for s in re.split(' +', lines[1])[1:]]
    else:
        time = [int(''.join(re.split(' +', lines[0])[1:]))]
        distance = [int(''.join(re.split(' +', lines[1])[1:]))]
    return time, distance


def travelled_distance(button_ms, race_ms):
    return (race_ms - button_ms) * button_ms


def feasible_button_ms(race_ms, record_distance):
    result = []
    for i in range(race_ms + 1):
        distance = travelled_distance(i, race_ms)
        if distance > record_distance:
            result.append(distance)
    return result


def get_winning_button_ms(lines, version):
    time, distance = get_data(lines, version)
    winning_button_ms = []
    for i in range(len(time)):
        button_ms_list = feasible_button_ms(time[i], distance[i])
        winning_button_ms.append(len(button_ms_list))
    return winning_button_ms


print(np.prod(get_winning_button_ms(puzzle_input, 1)))

print(np.prod(get_winning_button_ms(puzzle_input, 2)))
