import os

with open('input.txt', 'r') as input_data:
    program = [line.strip() for line in input_data.readlines()]

cycle = 0
x_value = 1
sig_strengths = {}
signal_sum = 0
crt_out = [[]]


def calc_sig():
    global sig_strengths, signal_sum
    sig_strengths[cycle] = cycle * x_value
    signal_sum += sig_strengths[cycle]
    # print(f"Signal strength after cycle {cycle} is {sig_strengths[cycle]}")


def draw_pixel():
    display_row = (cycle - 1) // 40
    if display_row >= len(crt_out):
        crt_out.append([])

    pixel_position = (cycle - 1) % 40
    sprite_positions = [x_value - 1, x_value, x_value + 1]
    # print(f"pixel at {pixel_position}, sprite at {sprite_positions}")

    if pixel_position in sprite_positions:
        crt_out[display_row].append('#')
    else:
        crt_out[display_row].append('.')


def add_cycle(x):
    global cycle
    for i in range(x):
        cycle += 1
        if (cycle + 20) % 40 == 0:
            calc_sig()
        draw_pixel()


def exec_noop():
    add_cycle(1)
    pass


def exec_addx(x):
    global x_value
    add_cycle(2)
    x_value += x


def handle_command(command):
    if command.startswith("noop"):
        exec_noop()
    elif command.startswith("addx"):
        exec_addx(int(command.split()[1]))
    else:
        pass


for command in program:
    handle_command(command)

print(f"Part 1: Sum of signals is {signal_sum}\n")

print(f"Part 2:")

for line in crt_out:
    print("".join(line))
