#!/usr/bin/env python3

import os

input_path = os.path.join(os.path.dirname(__file__), "01-input.txt")

with open(input_path, "r") as input:
    a, b, c = [int(input.readline()) for x in range(3)]
    last_sum = a + b + c
    increased_sum_count = 0

    for measurement in input:
        a, b, c, = b, c, int(measurement)
        current_sum = a + b + c

        if current_sum > last_sum:
            increased_sum_count += 1

        last_sum = current_sum

print(f'increased sum count:\t{increased_sum_count}')
