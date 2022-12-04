with open("input.txt", "r") as input_data:
    pairs = input_data.readlines()
    pairs = [pair.strip() for pair in pairs]

print(pairs)

fully_contained_pairs = 0
partial_overlap = 0

for pair in pairs:
    elf1 = pair.split(',')[0]
    elf1_range = [*range(int(elf1.split('-')[0]), int(elf1.split('-')[-1]) + 1)]
    elf2 = pair.split(',')[1]
    elf2_range = [*range(int(elf2.split('-')[0]), int(elf2.split('-')[-1]) + 1)]
    if set(elf1_range) <= set(elf2_range) or set(elf2_range) <= set(elf1_range):
        print(f"{elf1} and {elf2} have complete overlap.")
        fully_contained_pairs += 1
        partial_overlap += 1
    elif not set(elf1_range).isdisjoint(set(elf2_range)) or not set(elf2_range).isdisjoint(set(elf1_range)):
        print(f"{elf1} and {elf2} have partial overlap.")
        partial_overlap += 1
    else:
        print(f"{elf1} and {elf2} have no overlap.")


print(f"Total excessive pairs: {fully_contained_pairs}\n"
      f"Partial overlap: {partial_overlap}")



