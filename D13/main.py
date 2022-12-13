def packets_to_pairs(raw_packets):
    pair = []
    pairs = []

    for line in packets:
        if line == '':
            pairs.append(pair)
            pair = []
        else:
            pair.append(eval(line))
    if pair:
        pairs.append(pair)

    return pairs


def packets_with_divider(raw_packets):
    all_packets = []

    for line in packets:
        if line == '':
            pass
        else:
            all_packets.append(eval(line))

    all_packets += [[2]], [[6]]
    return all_packets


def compare_int(left, right):
    if left < right:
        return True
    if left > right:
        return False
    if left == right:
        return None


def compare_list(left, right):
    left_length = len(left)
    right_length = len(right)
    i = 0
    while True:
        if i == left_length and i == right_length:
            return
        elif i == left_length:
            return True
        elif i == right_length:
            return False

        left_item = left[i]
        right_item = right[i]

        if type(left_item) is int and type(right_item) is int:
            is_ordered = compare_int(left_item, right_item)
        elif type(left_item) is int:
            is_ordered = compare_list([left_item], right_item)
        elif type(right_item) is int:
            is_ordered = compare_list(left_item, [right_item])
        else:
            is_ordered = compare_list(left_item, right_item)

        if is_ordered is not None:
            return is_ordered

        i += 1


def compare_pairs(list_of_pairs: list):
    ordered = []
    total_ordered = 0
    for index, pair in enumerate(list_of_pairs):
        if compare_list(pair[0], pair[1]):
            total_ordered += 1
            ordered.append(index + 1)
    return ordered, total_ordered


def sort_packets(list_of_packets):
    is_ordered = False
    ordered_packets = [packet for packet in list_of_packets]
    while not is_ordered:
        is_ordered = True
        for i in range(len(ordered_packets) - 1):
            in_order = compare_list(ordered_packets[i], ordered_packets[i + 1])
            # in_order can be None if the packets are equivalent
            if not in_order:
                ordered_packets[i], ordered_packets[i + 1] = ordered_packets[i + 1], ordered_packets[i]
                is_ordered = False
    return ordered_packets


with open('input.txt') as data:
    packets = [line.strip() for line in data.readlines()]

packet_pairs = packets_to_pairs(packets)
packet_list = packets_with_divider(packets)
ordered_pair_indexes, total_ordered_pairs = compare_pairs(packet_pairs)
sorted_packets = sort_packets(packet_list)

divider_packet_2 = sorted_packets.index([[2]]) + 1
divider_packet_6 = sorted_packets.index([[6]]) + 1

print(f"P1: Total ordered: {total_ordered_pairs}, indexes: {ordered_pair_indexes}, sum: {sum(ordered_pair_indexes)}")

print(f"P2: Sum of dividers: {divider_packet_6} + {divider_packet_2} = {divider_packet_6 * divider_packet_2}")

