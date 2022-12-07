import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

def get_range(assignment: str):
    bounds = [int(section) for section in assignment.split('-')]
    return range(bounds[0],bounds[1]+1,1)

def get_ranges(line: str):
    return [get_range(assignment) for assignment in line.split(',')]

total_contained = 0
for line in lines:
    ranges = get_ranges(line)
    if set(ranges[0]).issubset(ranges[1]) or set(ranges[1]).issubset(ranges[0]):
        total_contained += 1

print(total_contained)

total_overlap = 0
for line in lines:
    ranges = get_ranges(line)
    if len(set(ranges[0]).intersection(ranges[1])) > 0:
        total_overlap += 1

print(total_overlap)