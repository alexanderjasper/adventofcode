import os
import sys
with open(os.path.join(sys.path[0], "input.txt"), "r") as f:
    lines = f.read().splitlines()

def get_full_path(path_list):
    return '/' + '/'.join(path_list)

def run_line(line, current_path):
    words = line.split(' ')
    if words[0] == '$' and words[1] == 'cd':
        if words[2] == '..':
            current_path.pop()
        elif words[2] == '/':
            current_path = []
        else:
            current_path.append(words[2])
    elif words[0] == '$' and words[1] == 'ls':
        return
    elif words[0] == 'dir':
        dir_name = line[4:]
        dir_path = get_full_path(current_path + [dir_name])
        directories[dir_path] = []
    else:
        file_size = int(words[0])
        file_name = words[1]
        directories[get_full_path(current_path)].append([file_name,file_size])

directories = {'/': []}
current_path = []
for line in lines:
    run_line(line, current_path)

def get_dir_size(dir_key, all_dirs):
    total_size = 0
    for key in all_dirs:
        if key.startswith(dir_key):
            for file in all_dirs[key]:
                total_size += file[1]
    return total_size

total_at_most_100k = 0
for key in directories:
    size = get_dir_size(key, directories)
    if size <= 100_000:
        total_at_most_100k += size

print(total_at_most_100k)

filesystem_available = 70000000
min_free_space = 30000000
total_size = get_dir_size('/', directories)
required_to_remove = total_size-filesystem_available+min_free_space

dirs_large_enough = []
for key in directories:
    size = get_dir_size(key, directories)
    if size >= required_to_remove:
        dirs_large_enough.append(size)
print(min(dirs_large_enough))