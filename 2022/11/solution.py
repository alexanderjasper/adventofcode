import os
import sys
import numpy as np
import math
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_monkeys(lines):
    monkeys = []
    num_of_monkeys = math.ceil(len(lines)/7)
    for i in range(num_of_monkeys):
        line_no = i * 7
        starting_items = [int(item)
                          for item in lines[line_no+1][18:].split(', ')]
        formula = lines[line_no+2][19:]
        test = int(lines[line_no+3][21:])
        if_true = int(lines[line_no+4][29:])
        if_false = int(lines[line_no+5][30:])
        monkeys.append({
            'items': starting_items,
            'formula': formula,
            'test': test,
            'true': if_true,
            'false': if_false,
            'inspections': 0})
    return monkeys


def monkey_business(monkeys):
    inspection_nos = list([monkey['inspections'] for monkey in monkeys])
    inspection_nos.sort(reverse=True)
    return inspection_nos[0]*inspection_nos[1]


rounds = 20
monkeys = get_monkeys(lines)
for _ in range(rounds):
    for monkey in monkeys:
        items = monkey['items']
        for i in range(len(items)):
            monkey['inspections'] += 1
            old = items.pop(0)
            new = math.floor(eval(monkey['formula'])/3)
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)
print(monkey_business(monkeys))


rounds = 10000
monkeys = get_monkeys(lines)
lcm = math.lcm(*[int(monkey['test']) for monkey in monkeys])
for _ in range(rounds):
    for monkey in monkeys:
        items = monkey['items']
        for i in range(len(items)):
            monkey['inspections'] += 1
            old = items.pop(0)
            new = math.floor(eval(monkey['formula']) % lcm)
            if new % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(new)
            else:
                monkeys[monkey['false']]['items'].append(new)

print(monkey_business(monkeys))
