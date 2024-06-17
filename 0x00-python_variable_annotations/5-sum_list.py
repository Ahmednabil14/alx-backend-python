#!/usr/bin/env python3
"""task 5"""


def sum_list(input_list: list[float]) -> float:
    sum: float = 0
    for li in input_list:
        sum += li
    return sum
