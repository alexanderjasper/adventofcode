import os
import sys
import numpy as np
from itertools import takewhile
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

grid = np.array([list(map(int, [*line])) for line in lines])


def can_see_over(tree, other_trees):
    return tree > max(other_trees, default=-1)


def views(r, c, grid):
    return [np.flip(grid[:r, c]),
            grid[r+1:, c],
            np.flip(grid[r, :c]),
            grid[r, c+1:]]


def is_visible(r, c, grid):
    tree = grid[r, c]
    return any([can_see_over(tree, sight) for sight in views(r, c, grid)])


def number_of_visible(grid):
    count = 0
    for r, c in np.ndindex(*grid.shape):
        count += is_visible(r, c, grid)
    return count


print(number_of_visible(grid))


def viewing_distance(view, tree):
    return min(len(list(takewhile(lambda t: t < tree, view)))+1, len(view))


def scenic_score(r, c, grid):
    return np.prod(
        [viewing_distance(view, grid[r, c]) for view in views(r, c, grid)]
    )


print(max([scenic_score(r, c, grid) for r, c in np.ndindex(*grid.shape)]))
