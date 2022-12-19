import numpy as np


def parse_input(input_file):
    with open(input_file) as data:
        cubes = set()

        min_val = 999999999
        max_val = -1

        for line in data.readlines():
            x, y, z = map(int, line.strip().split(','))
            cubes.add((x, y, z))

            for value in [x, y, z]:
                min_val = min(min_val, value)
                max_val = max(max_val, value)

    return cubes, (min_val, max_val)


def part_1(cubes):
    ans = 0
    for x, y, z in cubes:
        covered = 0
        position = np.array((x, y, z))

        for i in range(3):
            pos_next = np.array((0, 0, 0))
            pos_next[i] = 1

            if tuple(position + pos_next) in cubes:
                covered += 1

            pos_prev = np.array((0, 0, 0))
            pos_prev[i] = 1

            if tuple(position + pos_prev) in cubes:
                covered += 1

        ans += 6 - covered
    return ans


droplets, size = parse_input('Input.txt')
print(f"Input min - max: {size}")

print(f"Part 1: {part_1(droplets)}")

