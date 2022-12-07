import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

for index, line in enumerate(lines):
    if '[' not in line:
        stack_lines = index
        break
number_of_stacks = int(lines[stack_lines][-2])


def get_crates_in_line(line, number_of_stacks):
    crates = ''
    for i in range(number_of_stacks):
        if len(line) > 1+4*i:
            crates += line[1+4*i]
        else:
            crates += ' '
    return crates.replace(' ', '-')

def get_stacks(lines):
    stacks = [[] for _ in range(number_of_stacks)]
    for i in reversed(range(stack_lines)):
        line = lines[i]
        crates = get_crates_in_line(line, number_of_stacks)
        for index, char in enumerate(crates):
            if char != '-':
                stacks[index].append(char)
    return stacks


def run_sequence(line, stacks, multiple_at_once=False):
    split_line = line.split(' ')
    amount_to_move = int(split_line[1])
    move_from = int(split_line[3])-1
    move_to = int(split_line[5])-1
    if multiple_at_once:
        crates = stacks[move_from][-amount_to_move:]
        del stacks[move_from][-amount_to_move:]
        stacks[move_to].extend(crates)
    else:
        for _ in range(amount_to_move):
            crate = stacks[move_from].pop()
            stacks[move_to].append(crate)


stacks_1 = get_stacks(lines)
for i in range(stack_lines+2, len(lines)):
    run_sequence(lines[i], stacks_1)

result_1 = ''
for stack in stacks_1:
    result_1 += stack[-1]

print(result_1)


stacks_2 = get_stacks(lines)
for i in range(stack_lines+2, len(lines)):
    run_sequence(lines[i], stacks_2, True)

result_2 = ''
for stack in stacks_2:
    result_2 += stack[-1]

print(result_2)
