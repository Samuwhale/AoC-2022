import requests
import numpy as np
with open("input.txt", "r") as input:
    data = input.readlines()

numbers = []
elfs = 0
numbers.append([])
for line in data:
    if line != '\n':
        number = int(line.strip())
        numbers[elfs].append(number)
    else:
        elfs += 1
        numbers.append([])

sums = []
for element in numbers:
    sums.append(np.sum(element))

sums.sort(reverse=True)
# Step 1: Get the single highest value
print(f"The highest value is: {sums[0]}")

# Step 2: Get the sum of the top three values
top3 = sums[:3]
print(f"The highest three values are: {top3}, totaling up to: {np.sum(top3)}")






