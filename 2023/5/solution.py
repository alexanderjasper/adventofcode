import os
import sys

with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    puzzle_input = f.read()


def get_seeds(document):
    str_values = document.split('\n\n')[0].split(': ')[1].split(' ')
    int_values = [int(s) for s in str_values]
    return int_values


def get_maps(document):
    maps_sections = document.split('\n\n')[1:]

    def get_map(section):
        lines = section.split('\n')[1:]

        def get_range_map(line):
            str_values = line.split(' ')
            int_values = [int(n) for n in str_values]
            return int_values

        seed_map = [get_range_map(ln) for ln in lines if ln != '']
        return seed_map

    seed_maps = [get_map(section) for section in maps_sections]
    return seed_maps


def range_intersect(r1, r2):
    return range(max(r1.start, r2.start), min(r1.stop, r2.stop)) or None


def range_diff(r1, r2):
    endpoints = sorted((r1.start, r1.stop, r2.start, r2.stop))
    result = []
    if endpoints[0] == r1.start and endpoints[1] != r1.start:
        result.append(range(endpoints[0], endpoints[1]))
    if endpoints[3] == r1.stop and endpoints[2] != r1.stop:
        result.append(range(endpoints[2], endpoints[3]))
    return result


def range_add(r, n):
    return range(r.start + n, r.stop + n)


def apply_map(seed_range, seed_map):
    for map_range in seed_map:
        destination_start, source_start, length = map_range
        map_source_range = range(source_start, source_start + length)
        shift = destination_start - source_start

        intersect = range_intersect(seed_range, map_source_range)

        if intersect is not None:
            diff = range_diff(seed_range, map_source_range)
            mapped_diff = [item for sublist in [apply_map(d, seed_map) for d in diff] for item in sublist]
            return mapped_diff + [range_add(intersect, shift)]
    return [seed_range]


def map_seed_ranges(srs, seed_maps):
    for seed_map in seed_maps:
        temp_ranges = []
        for seed_range in srs:
            result = apply_map(seed_range, seed_map)
            temp_ranges += result
        srs = temp_ranges
    return srs


def get_least_ending_point(srs, s_maps):
    mapped_seed_ranges = map_seed_ranges(srs, s_maps)
    starting_points = [r.start for r in mapped_seed_ranges]
    return min(starting_points)


seeds = get_seeds(puzzle_input)
seed_ranges = [range(s, s + 1) for s in seeds]
maps = get_maps(puzzle_input)
print(get_least_ending_point(seed_ranges, maps))


def get_seed_ranges(document):
    str_values = document.split('\n\n')[0].split(': ')[1].split(' ')
    int_values = [int(s) for s in str_values]
    seed_starts = int_values[::2]
    seed_range_lengths = int_values[1::2]
    return [range(seed_starts[i], seed_starts[i] + seed_range_lengths[i]) for i in range(len(seed_starts))]


seed_ranges = get_seed_ranges(puzzle_input)
print(get_least_ending_point(seed_ranges, maps))
