#!/usr/bin/env python3
from typing import List, Union
"""task 6"""


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum mixed list"""
    sum: float = 0
    for li in mxd_lst:
        sum += float(li)
    return sum
