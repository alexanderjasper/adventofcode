import os
import sys


def part1(puzzle_input):
    return f'Part 1: '


def part2(puzzle_input):
    return f'Part 2: '


def solve(input_file_path):
    with open(os.path.join(sys.path[0], input_file_path), "r") as f:
        lines = f.read().splitlines()
        print(input_file_path)
        print(part1(lines))
        print(part2(lines))


solve('test_input.txt')
solve('input.txt')
