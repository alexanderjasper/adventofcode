import os
import sys
import numpy as np
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def strength_at_cycle(lines, cycle_stop):
    X = 1
    cycle = 1
    for line in lines:
        if cycle == cycle_stop:
            return X * cycle
        cmd = line.split(' ')
        if cmd[0] == 'addx':
            cycle += 1
            if cycle == cycle_stop:
                return X * cycle
            X += int(cmd[1])
        cycle += 1
    return X * cycle


checkpoints = np.add(np.multiply(range(6),40),20)
print(np.sum([strength_at_cycle(lines,checkpoint) for checkpoint in checkpoints]))

def sprite_visible(X, cycle, width):
    cycle_column = cycle % width
    leftmost_pixel = X
    return cycle_column in range (leftmost_pixel, leftmost_pixel+3)

def draw_pixel(screen, width, cycle, X):
    length_of_last_line = len(np.flip(screen.split('\n'))[0])
    if length_of_last_line == width:
        screen += '\n'
    if sprite_visible(X, cycle, width):
        screen += '#'
    else:
        screen += '.'
    return screen


def get_screen(lines, width):
    screen = ''
    X = 1
    cycle = 1
    for line in lines:
        screen = draw_pixel(screen, width, cycle, X)
        cycle += 1
        cmd = line.split(' ')
        if cmd[0] == 'addx':
            screen = draw_pixel(screen, width, cycle, X)
            cycle += 1
            X += int(cmd[1])
    return screen

print(get_screen(lines, 40))

