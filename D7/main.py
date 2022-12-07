import json
import numpy as np

with open('input.txt', 'r') as input_data:
    terminal_feed = [line.strip() for line in input_data.readlines()]

directories = {"/":
    {
        'files': {}
    }
}
current_directory = directories["/"]
path = []
all_directories = []
sum_of_sizes = 0


def move_to_parent_dir():
    global path, current_directory
    path = path[:-1]
    print(f"path: {path}")
    current_directory = directories["/"]
    if len(path) > 0:
        for dir in path:
            current_directory = current_directory[dir]
    print(f"Moving into parent dir: {current_directory}")


def move_to_outer_dir():
    global current_directory, path
    current_directory = directories["/"]
    path = []
    print(f"Moving into base dir: {current_directory}")


def move_into_dir():
    global current_directory, path
    dir_name = line.split(' ')[2]
    current_directory[dir_name] = {}
    current_directory = current_directory[dir_name]
    current_directory['files'] = {}
    path.append(dir_name)
    if not current_directory in all_directories:
        all_directories.append(current_directory)


for line in terminal_feed:
    print(line)
    if line.startswith('$ cd'):
        if line.startswith('$ cd ..'):
            move_to_parent_dir()
        elif line.startswith('$ cd /'):
            move_to_outer_dir()
        else:
            move_into_dir()
    elif line.startswith('$ ls'):
        pass
    else:
        file_name = line.split(' ')[1]
        file_size = line.split(' ')[0]
        if file_size != 'dir':
            file_size = int(file_size)
            current_directory['files'][file_name] = file_size


def get_sum_of_files(file_dict):
    internal_sum = 0
    for file, filesize in file_dict.items():
        internal_sum += filesize
    return internal_sum


def get_directory_size(directory_dict):
    total_sum = 0
    for dir_name, dir_dict in directory_dict.items():
        if dir_name == 'files':
            total_sum += get_sum_of_files(dir_dict)
        elif type(dir_dict) is dict:
            total_sum += get_directory_size(dir_dict)
    return total_sum


print(json.dumps(directories, sort_keys=True, indent=4))


def get_sum_of_sizes():
    internal_sum = 0
    for directory in all_directories:
        if get_directory_size(directory) <= 100000:
            internal_sum += get_directory_size(directory)
    return internal_sum


def get_dir_matching_size(size_req):
    internal_sum = 0
    lowest = 999999999999
    matching_dirs = []
    for directory in all_directories:
        dir_size = get_directory_size(directory)
        if dir_size >= size_req:
            if dir_size < lowest:
                lowest = dir_size
    return lowest


print(all_directories)

sum_of_sizes = get_sum_of_sizes()
total_size = get_directory_size(directories)
unused_space = 70000000 - total_size
amount_to_delete = 30000000 - unused_space
print(f"Part 1: Sum of sizes from dirs under 100000: {sum_of_sizes}.")
print(f"Part 2: Total size is {total_size}, remaining size is: {unused_space}.\n"
      f"Delete {amount_to_delete} to update.")
print(f"Part 2 solution: {get_dir_matching_size(amount_to_delete)}")
