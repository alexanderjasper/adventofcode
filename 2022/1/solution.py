import os
import sys
import numpy as np
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.readlines()

elf_totals = np.array([0])
for line in lines:
    if line == "\n":
        elf_totals = np.append(elf_totals,[0])
    else:
        elf_totals[len(elf_totals)-1] += int(line)

max = np.max(elf_totals)
print(max)

sorted = np.flip(np.sort(elf_totals))
top_three = np.sum(sorted[:3])
print(top_three)