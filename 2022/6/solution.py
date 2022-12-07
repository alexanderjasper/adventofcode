import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()
line = lines[0]

def all_characters_unique(string):
    previous_characters = set()
    for char in string:
        if char in previous_characters:
            return False
        previous_characters.add(char)
    return True

def find_marker(input, chars_required):
    for i in range(len(input)-chars_required):
        if all_characters_unique(input[i:i+chars_required]):
            return i+chars_required
    raise Exception("No marker.")

print(find_marker(line, 4))

print(find_marker(line, 14))
