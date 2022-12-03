# Convoluted way of not having to manually type out a list
azAZ = "abcdefghijklmnopqrstuvwxyz"
azAZ+=azAZ.upper()
azAZ = [char for char in azAZ]


with open("input.txt", "r") as input_data:
    input = input_data.read()
    rucksacks = input.split('\n')

print(rucksacks)


def get_score(item):
    return azAZ.index(item) + 1


total_score = 0

# Step 1
for rucksack in rucksacks:
    first_comp = rucksack[:(len(rucksack)//2)]
    second_comp = rucksack[len(rucksack)//2:]
    shared_items = []
    for item in first_comp:
        if item in second_comp and not item in shared_items:
            shared_items.extend(item)

    score = 0
    for item in shared_items:
        item_score = get_score(item)
        score += item_score

    total_score += score

print(f"Exercise 1: {total_score}")

# Step 2
group = 0
grouped_rucksacks = [[]]

for index, rucksack in enumerate(rucksacks):
    if index != 0 and index % 3 == 0:
        group += 1
        grouped_rucksacks.append([])
    grouped_rucksacks[group].append(rucksack)

badges = []

for group_number, backpacks in enumerate(grouped_rucksacks):
    badge = []
    for item in backpacks[0]:
        if item in backpacks[1] and item in backpacks[2] and item not in badge:
            badge = item

    badges.extend(badge)

badge_total = 0
for badge in badges:
    badge_total += get_score(badge)

print(f"Exercise 2: {badge_total}")



