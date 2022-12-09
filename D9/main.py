with open('input.txt', 'r') as input_data:
    instructions = [[line.strip().split()[0], int(line.strip().split()[1])] for line in input_data.readlines()]

visited = [(0, 0)]

directions = {
    "U": (0, 1),
    "D": (0, -1),
    "L": (-1, 0),
    "R": (1, 0)
}


def set_knots(amount):
    rope = [str(i + 1) for i in range(amount)]
    rope.insert(0, "H")
    return rope


rope = set_knots(9)
rope_positions = {knot: (0, 0) for knot in rope}


def add_coordinates(set1: tuple, set2: tuple):
    return set1[0] + set2[0], set1[1] + set2[1]


def get_distance(point: tuple, destination: tuple):
    return abs(point[0] - destination[0]), abs(point[1] - destination[1])


def get_direction(point: tuple, destination: tuple):
    x = destination[0] - point[0]
    y = destination[1] - point[1]
    if x > 1:
        x = 1
    if y > 1:
        y = 1
    if x < -1:
        x = -1
    if y < -1:
        y = -1
    return x, y


def move_head(direction):
    global rope_positions
    rope_positions["H"] = add_coordinates(rope_positions["H"], directions[direction])


def move_knot(knot):
    knot_pos = rope_positions[knot]
    previous_knot_pos = rope_positions[rope[rope.index(knot) - 1]]
    distance = get_distance(knot_pos, previous_knot_pos)
    direction = get_direction(knot_pos, previous_knot_pos)
    print(f"{knot} was at: {knot_pos}, dist: {distance}, dir: {direction}...")
    if distance[0] > 1 or distance[1] > 1:
        knot_pos = add_coordinates(knot_pos, direction)
        rope_positions[knot] = knot_pos
    print(f"...{knot} now at: {knot_pos}\n")


def handle_instruction(direction, amount):
    print(f"Handling instruction '{direction} {amount}':")
    for step in range(amount):
        print(f"\nMoving {direction}: {step + 1}/{amount}\nhead was at: {rope_positions['H']}...")
        move_head(direction)
        print(f"...is now at: {rope_positions['H']}\n")
        for knot in rope[1:]:
            move_knot(knot)
        if not rope_positions[rope[-1]] in visited:
            visited.append(rope_positions[rope[-1]])
    print(f"\n")


for instruction in instructions:
    handle_instruction(instruction[0], instruction[1])

print(f"{len(visited)} tail positions.")
