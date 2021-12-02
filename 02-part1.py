#!/usr/bin/env python3

import os

input_path = os.path.join(os.path.dirname(__file__), "02-input.txt")

horizontal_pos = 0
depth = 0

with open(input_path, "r") as input:
    for line in input:
        movement, units = line.split()

        if movement == "forward":
            horizontal_pos += int(units)
        elif movement == "down":
            depth += int(units)
        elif movement == "up":
            depth -= int(units)

print(f'horizontal pos:\t{horizontal_pos}')
print(f'depth:\t{depth}')
print(f'result:\t{horizontal_pos * depth}')
