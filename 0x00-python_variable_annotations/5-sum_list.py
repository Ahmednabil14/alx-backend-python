#!/usr/bin/env python3
"""task 5"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """the sum of list"""
    sum: float = 0
    for li in input_list:
        sum += li
    return sum
