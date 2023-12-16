import os
import string
import sys

import numpy as np


def get_instructions(puzzle_input):
    instructions_str = puzzle_input[0]
    instructions_bits = [0 if c == 'L' else 1 for c in instructions_str]
    return instructions_bits


def convert_to_number(node):
    components = [string.ascii_uppercase.index(c) for c in node]
    base26_components = [c * 26 ** idx for idx, c in enumerate(reversed(components))]
    return np.sum(base26_components)


def get_maps(puzzle_input):
    maps = {}
    for line in puzzle_input[2:]:
        node = convert_to_number(line.split(' ')[0])
        left = convert_to_number(line.split('(')[1].split(',')[0])
        right = convert_to_number(line.split('(')[1].split(',')[1][1:].split(')')[0])
        maps[node] = (left, right)
    return maps


def part1(puzzle_input):
    instructions = get_instructions(puzzle_input)
    maps = get_maps(puzzle_input)
    goal = convert_to_number('ZZZ')

    steps = 0
    position = 0
    while position < goal:
        for instruction in instructions:
            position = maps[position][instruction]
            steps += 1
            if position == goal:
                break
    return f'Part 1: {steps}'


def get_loop_length(starting_position, maps, instructions):
    position = starting_position
    steps = 0
    while position % 26 != 25:
        for instruction in instructions:
            position = maps[position][instruction]
            steps += 1
            if position % 26 == 25:
                break
    return steps


def part2(puzzle_input):
    instructions = get_instructions(puzzle_input)
    maps = get_maps(puzzle_input)

    loop_lengths = [get_loop_length(p, maps, instructions) for p in maps.keys() if p % 26 == 0]
    result = np.lcm.reduce(loop_lengths)
    return f'Part 2: {result}'


def solve(input_file_path):
    with open(os.path.join(sys.path[0], input_file_path), "r") as f:
        lines = f.read().splitlines()
        print(input_file_path)
        print(part1(lines))
        print(part2(lines))

solve('test_input_1.txt')
solve('test_input_2.txt')
solve('input.txt')
