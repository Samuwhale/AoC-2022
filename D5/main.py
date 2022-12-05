with open("input.txt", "r") as input_data:
    input_data = input_data.readlines()

crates = []
moves = []


def get_moves(input):
    internal_moves = []
    for line in input:
        if line.startswith('move'):
            line = line.strip()
            internal_moves.append(line)
    return internal_moves


def get_crates(input):
    crate_lines = []
    crate_stacks = []
    amount_of_stacks = 0
    for line in input:
        if not line.startswith('move'):
            if not line.startswith(' 1'):
                crate_lines.append(line)
            elif line.startswith(' 1'):
                print(f"numline : {line}")
                try:
                    amount_of_stacks = int(line.split(' ')[-1])
                except:
                    amount_of_stacks = int(line.split(' ')[-2])
                print(f"Amount of stacks: {amount_of_stacks}")
    for i in range(0, amount_of_stacks):
        print(f"I is = {i}")
        crate_stacks.append([])

    for line in crate_lines:
        for i in range(0, amount_of_stacks):
            try:
                letter = line[i * 4 + 1]
                if letter != ' ': crate_stacks[i].append(letter.strip())
            except:
                pass
    return crate_stacks, amount_of_stacks


def get_top_crates(input_crates, move_list):
    print(f"Cratemover 9000: ")
    print(f"Starting with {input_crates}")
    for move in move_list:
        amount = int(move.split(' ')[1])
        source = int(move.split(' ')[3]) - 1
        target = int(move.split(' ')[5]) - 1

        for _ in range(amount):
            input_crates[target].insert(0, input_crates[source][0])
            input_crates[source].pop(0)

        print(f"moving: {amount}, from: {source}, to: {target}. Resulting in: {input_crates}")

    top_crates = []
    for crate in input_crates:
        top_crates.extend(crate[0])

    top_crates = ''.join(top_crates)
    print(f"The top ones are: {top_crates}")
    print(f"Ending with {input_crates}")
    return top_crates


def get_top_crates_two(input_crates, move_list):
    print(f"Cratemover 9000: ")
    print(f"Starting with {input_crates}")
    for move in move_list:
        amount = int(move.split(' ')[1])
        source = int(move.split(' ')[3]) - 1
        target = int(move.split(' ')[5]) - 1
        inbetween = []
        input_crates[target] = input_crates[source][:amount] + input_crates[target]
        for _ in range(amount):
            input_crates[source].pop(0)




        print(f"moving: {amount}, from: {source}, to: {target}. Resulting in: {input_crates}")

    top_crates = []
    for crate in input_crates:
        top_crates.extend(crate[0])

    top_crates = ''.join(top_crates)
    print(f"The top ones are: {top_crates}")

    return top_crates


moves = get_moves(input_data)
crates, stack_amount = get_crates(input_data)

# mover_9000 = get_top_crates(crates, moves)
mover_9001 = get_top_crates_two(crates, moves)
