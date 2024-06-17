#!/usr/bin/env python3
from typing import List
"""task 5"""


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for li in input_list:
        sum += li
    return sum
