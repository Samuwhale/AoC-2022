with open('input.txt') as input_data:
    signal = input_data.read().strip()


def is_unique(values):
    temp_set = set()
    for char in values:
        if char in temp_set:
            return False
        else:
            temp_set.add(char)
    return True


def get_unique_segment(raw_signal, segment_length: int):
    last_items = []
    iterations = 0
    for char in signal:
        if len(last_items) >= segment_length:
            last_items.pop(0)
        last_items.extend(char)
        iterations += 1
        if is_unique(last_items) and len(last_items) == segment_length:
            print(
                f"After {iterations} characters, unique part of length {segment_length} was found in: {''.join(last_items)}")
            break


# Part 1
get_unique_segment(signal, 4)

# Part 2
get_unique_segment(signal, 14)
