#!/usr/bin/env python3

import os

input_path = os.path.join(os.path.dirname(__file__), "01-input.txt")

with open(input_path, "r") as input:
    last = int(input.readline())
    increased_measurement_count = 0

    for measurement in input:
        current = int(measurement)

        if current > last:
            increased_measurement_count += 1

        last = current

print(f'increased measurement count:\t{increased_measurement_count}')
