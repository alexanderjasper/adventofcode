import os
import sys

import numpy as np
from dijkstar import find_path, Graph


def get_node_number(grid, row, col, node_type) -> int:
    """type == 0: can move vertically, type == 1: can move horizontally"""
    base_node_number = row * grid.shape[0] + col
    if node_type == 1:
        return base_node_number + grid.size
    return base_node_number


def get_distance(grid, from_node, to_node) -> int:
    traversed_nodes = []
    for r in range(min(from_node[0], to_node[0]), max(from_node[0], to_node[0] + 1)):
        for c in range(min(from_node[1], to_node[1]), max(from_node[1], to_node[1] + 1)):
            node = (r, c)
            if node != from_node:
                traversed_nodes.append(node)
    return np.sum([grid[*node] for node in traversed_nodes])


def get_lowest_cost(grid, min_blocks_move, max_blocks_move) -> int:
    graph = Graph()
    for row in range(grid.shape[0]):
        for col in range(grid.shape[1]):
            # Add vertical moves from type 0 -> type 1
            vertical_moves = (
                    list(range(min_blocks_move * (- 1), -1 - min(row, max_blocks_move), -1)) +
                    list(range(min_blocks_move, 1 + min(grid.shape[0] - row - 1, max_blocks_move)))
            )
            for m in vertical_moves:
                distance = get_distance(grid, (row, col), (row + m, col))
                from_node_n = get_node_number(grid, row, col, 0)
                to_node_n = get_node_number(grid, row + m, col, 1)
                graph.add_edge(from_node_n, to_node_n, distance)
                # graph[from_node_n] = graph[from_node_n] + [(to_node_n, distance)]

            # Add horizontal moves from type 1 -> type 0
            horizontal_moves = (
                    list(range(min_blocks_move * (-1), -1 - min(col, max_blocks_move), -1)) +
                    list(range(min_blocks_move, 1 + min(grid.shape[1] - col - 1, max_blocks_move)))
            )
            for m in horizontal_moves:
                distance = get_distance(grid, (row, col), (row, col + m))
                from_node_n = get_node_number(grid, row, col, 1)
                to_node_n = get_node_number(grid, row, col + m, 0)
                graph.add_edge(from_node_n, to_node_n, distance)
                # graph[from_node_n] = graph[from_node_n] + [(to_node_n, distance)]

    # Create main start/end nodes with edges (of 0 cost) into both copies (type 0 + 1) of the grid
    start_node_type_0 = get_node_number(grid, 0, 0, 0)
    start_node_type_1 = get_node_number(grid, 0, 0, 1)
    end_node_type_0 = get_node_number(grid, grid.shape[0] - 1, grid.shape[1] - 1, 0)
    end_node_type_1 = get_node_number(grid, grid.shape[0] - 1, grid.shape[1] - 1, 1)
    main_start_node = end_node_type_1 + 1
    main_end_node = end_node_type_1 + 2
    graph.add_edge(main_start_node, start_node_type_0, 0)
    graph.add_edge(main_start_node, start_node_type_1, 0)
    graph.add_edge(end_node_type_0, main_end_node, 0)
    graph.add_edge(end_node_type_1, main_end_node, 0)

    shortest_path = find_path(graph, main_start_node, main_end_node)
    return shortest_path.total_cost


def part1(puzzle_input):
    grid = np.array([[int(c) for c in line] for line in puzzle_input])
    lowest_cost = get_lowest_cost(grid, 1, 3)
    return f'Part 1: {lowest_cost}'


def part2(puzzle_input):
    grid = np.array([[int(c) for c in line] for line in puzzle_input])
    lowest_cost = get_lowest_cost(grid, 4, 10)
    return f'Part 2: {lowest_cost}'


def solve(input_file_path):
    with open(os.path.join(sys.path[0], input_file_path), "r") as f:
        lines = f.read().splitlines()
        print(input_file_path)
        print(part1(lines))
        print(part2(lines))


solve('test_input.txt')
solve('input.txt')
