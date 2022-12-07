import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()


def get_priority(character: str):
    raw_order = ord(character.lower()) - 96
    if character.islower():
        return raw_order
    else:
        return raw_order + 26


def get_common_letter(list_of_strings):
    sets = [set(string) for string in list_of_strings]
    return list(set.intersection(*sets))[0]


total_item_priority = 0
for line in lines:
    total_item_priority += get_priority(get_common_letter(
        [line[:int(len(line)/2)], line[int(len(line)/2):]]))

print(total_item_priority)


total_badge_priority = 0
for i in range(int(len(lines)/3)):
    group = lines[3*i:3*i+3]
    total_badge_priority += get_priority(get_common_letter(group))

print(total_badge_priority)