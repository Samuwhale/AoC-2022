import numpy as np


def signal_to_sensors(input_signal):
    sensors = {}
    for reading in input_signal:
        sensor = int(reading.split()[2].split('=')[1].split(',')[0]), int(
            reading.split()[3].split('=')[1].split(':')[0])
        beacon = int(reading.split()[-2].split('=')[1].split(',')[0]), int(reading.split()[-1].split('=')[1].split()[0])
        sensors[sensor] = beacon
        # print(f"Sensor {sensor}, beacon {beacon}, radius {distance}")
    return sensors


def manh_dist(point_a, point_b):
    distance = np.abs(point_b[0] - point_a[0]) + np.abs(point_b[1] - point_a[1])
    return distance


# def total_range(ranges):
#     total_area = 0
#     for i, (start, end) in enumerate(ranges):
#         for j in range(i + 1, len(ranges)):
#             overlap_start = max(start, ranges[j][0])
#             overlap_end = min(end, ranges[j][1])
#             if overlap_start < overlap_end:
#                 total_area -= overlap_end - overlap_start
#         total_area += end - start
#     return total_area

def total_range(ranges, beacons):
    beacon_occupied_x = [beacon[0] for beacon in beacons]
    ans = 0
    lowest = min([i[0] for i in ranges])
    highest = max([i[1] for i in ranges])
    for x in range(lowest, highest + 1):
        if not x in beacon_occupied_x:
            for left, right in ranges:
                if left <= x <= right:
                    ans += 1
                    break
    return ans


def check_single_row(input_sensors, y_to_check):
    y = y_to_check
    occupied = []
    beacons = []
    for sensor, nearest_beacon in input_sensors.items():
        distance = manh_dist(sensor, nearest_beacon)
        if (sensor[1] - distance) <= y <= (sensor[1] + distance):
            width_at_y = abs(distance - abs(sensor[1] - y))
            left = sensor[0] - width_at_y
            right = sensor[0] + width_at_y
            occupied.append((left, right))

            if nearest_beacon[1] == y:
                if (sensor[0] - width_at_y) <= nearest_beacon[0] <= sensor[0] + width_at_y:
                    if not nearest_beacon in beacons:
                        beacons.append(nearest_beacon)
                        print(f"Beacon {nearest_beacon} found at Y={y}")

    occupied_area = total_range(occupied, beacons)

    return occupied_area


def check_excluded_zone(sensor_data):
    sensors = []
    beacons = []
    distances = []
    for sensor, beacon in sensor_data.items():
        sensors.append(sensor)
        beacons.append(beacon)
        distances.append(manh_dist(sensor, beacon))

    N = len(sensors)

    positive_lines = []
    negative_lines = []

    for index, sensor in enumerate(sensors):
        distance = distances[index]
        negative_lines.extend([sensor[0] + sensor[1] - distance, sensor[0] + sensor[1] + distance])
        positive_lines.extend([sensor[0] - sensor[1] - distance, sensor[0] - sensor[1] + distance])

    positive = None
    negative = None

    for i in range(2 * N):
        for j in range(i + 1, 2 * N):
            a, b = positive_lines[i], positive_lines[j]
            if abs(a - b) == 2:
                positive = 1 + min(a, b)

            a, b = negative_lines[i], negative_lines[j]

            if abs(a - b) == 2:
                negative = 1 + min(a, b)

    x, y = (positive + negative) // 2, (negative - positive) // 2
    ans = x * 4000000 + y
    return ans


with open('input.txt') as data:
    signal = [line.strip() for line in data.readlines()]

all_sensors = signal_to_sensors(signal)

print(f"Part 1: {check_single_row(all_sensors, 2000000)}")
print(f"Part 2: {check_excluded_zone(all_sensors)}")
