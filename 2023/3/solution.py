import os
import re
import sys

import numpy as np

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

puzzle_input = np.array([np.array([s for s in line]) for line in lines])


def is_symbol(char):
    return char != '.' and not char.isdigit()


def is_adjacent_to_symbol(index, input_matrix):
    row, col = index
    rows, cols = input_matrix.shape
    neighbors = []
    for row_adj in range(row - 1, row + 2):
        for col_adj in range(col - 1, col + 2):
            if 0 <= row_adj < rows and 0 <= col_adj < cols:
                neighbors.append(str(input_matrix[row_adj, col_adj]))
    return any([is_symbol(neighbor) for neighbor in neighbors])


def get_adjacent_to_symbol_matrix(schematic):
    adj_symbol_matrix = np.ndarray((140, 140))
    for index, element in np.ndenumerate(schematic):
        adj_symbol_matrix[index[0]][index[1]] = is_adjacent_to_symbol(index, schematic)
    return adj_symbol_matrix


def get_parts(schematic):
    parts = []
    adj_symbol_matrix = get_adjacent_to_symbol_matrix(schematic)
    for line_index, line in enumerate(lines):
        position = 0
        splits = re.split('[^0-9]', line)
        for split in splits:
            if split != '' and split[0].isdigit():
                start_pos = position
                end_pos = position + len(split)
                is_part = any(adj_symbol_matrix[line_index][start_pos:end_pos])
                if is_part:
                    parts.append((int(split), (line_index, (start_pos, end_pos))))
            position += len(split) + 1
    return parts


print(np.sum([part for part, placement in get_parts(puzzle_input)]))


def get_gear_ratios(schematic):
    parts = get_parts(schematic)
    gear_ratios = []
    for gear_index, element in np.ndenumerate(schematic):
        is_gear = element == '*'
        if is_gear:
            adjacent_parts = [
                part for part, part_index in parts if
                part_index[0] - 1 <= gear_index[0] <= part_index[0] + 1 and
                part_index[1][0] <= gear_index[1] + 1 and
                part_index[1][1] -1 >= gear_index[1] - 1
            ]
            if len(adjacent_parts) == 2:
                gear_ratio = np.prod(adjacent_parts)
                gear_ratios.append((gear_ratio, gear_index))
    return gear_ratios

print(np.sum([ratio for ratio, index in get_gear_ratios(puzzle_input)]))
