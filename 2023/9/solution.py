import os
import sys

import numpy as np


def get_histories(puzzle_input):
    values = np.array([np.array([int(n) for n in line.split(' ')]) for line in puzzle_input])
    return values


def get_sequences(history):
    sequences = [history]
    while any([v != 0 for v in sequences[-1]]):
        last_sequence = sequences[-1]
        derivative = []
        for i in range(1, len(sequences[-1])):
            derivative.append(last_sequence[i] - last_sequence[i - 1])
        sequences.append(derivative)
    return sequences


def get_prediction(history):
    sequences = get_sequences(history)
    return np.sum([s[-1] for s in sequences])


def part1(puzzle_input):
    histories = get_histories(puzzle_input)
    predictions = np.apply_along_axis(get_prediction, 1, histories)
    result = np.sum(predictions)
    return f'Part 1: {result}'


def get_extrapolation(history):
    sequences = get_sequences(history)
    first_values = [s[0] for s in sequences]
    result = np.sum(first_values[::2])-np.sum(first_values[1::2])
    return result


def part2(puzzle_input):
    histories = get_histories(puzzle_input)
    extrapolations = np.apply_along_axis(get_extrapolation, 1, histories)
    result = np.sum(extrapolations)
    return f'Part 2: {result}'


def solve(input_file_path):
    with open(os.path.join(sys.path[0], input_file_path), "r") as f:
        lines = f.read().splitlines()
        print(input_file_path)
        print(part1(lines))
        print(part2(lines))


solve('test_input.txt')
solve('input.txt')
