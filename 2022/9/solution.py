import os
import sys
import numpy as np
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_direction_and_distance(line):
    keys = line.split(' ')
    direction = [0, 0]
    match keys[0]:
        case 'U':
            direction = [0, 1]
        case 'D':
            direction = [0, -1]
        case 'L':
            direction = [-1, 0]
        case 'R':
            direction = [1, 0]
    return direction, int(keys[1])


def tail_follow(new_head, current_tail):
    new_tail = np.copy(current_tail)
    move_x = new_head[0] - current_tail[0]
    move_y = new_head[1] - current_tail[1]
    if abs(move_x) > 1 and abs(move_y) > 1:
        new_tail[0] += move_x/2
        new_tail[1] += move_y/2
        return new_tail
    if move_x > 1:
        new_tail[0] = new_head[0]-1
        new_tail[1] = new_head[1]
    if move_y > 1:
        new_tail[0] = new_head[0]
        new_tail[1] = new_head[1]-1
    if move_x < -1:
        new_tail[0] = new_head[0]+1
        new_tail[1] = new_head[1]
    if move_y < -1:
        new_tail[0] = new_head[0]
        new_tail[1] = new_head[1]+1
    return new_tail


def move_head(head_position, direction):
    return np.add(head_position, direction)


positions = []
head_position = [0, 0]
tail_position = [0, 0]
tail_positions = ['0,0']
for line in lines:
    direction, distance = get_direction_and_distance(line)
    for _ in range(distance):
        head_position = move_head(head_position, direction)
        tail_position = tail_follow(head_position, tail_position)
        positions.append(f'{tail_position[0]},{tail_position[1]}')
print(len(set(positions)))

import matplotlib.pyplot as plt
def plot_rope(rope):
    # plt.clf()
    # plt.xlim([-20,20])
    # plt.ylim([-20,20])
    # plt.scatter(*zip(*rope))
    # plt.pause(0.01)
    return

positions = []
positions_2 = []
rope = [[0, 0] for _ in range(10)]
for line in lines:
    direction, distance = get_direction_and_distance(line)
    for _ in range(distance):
        rope[0] = move_head(rope[0], direction)
        for i in range(1, 10):
            rope[i] = tail_follow(rope[i-1], rope[i])
        plot_rope(rope)
        positions.append(f'{rope[9][0]},{rope[9][1]}')
        positions_2.append(rope[9])
print(len(set(positions)))