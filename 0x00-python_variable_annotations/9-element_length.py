#!/usr/bin/env python3
"""task 9"""
from typing import Tuple, List, Iterable, Sequence


def element_length(lst: Iterable[Sequence]) -> List[tuple[Sequence, int]]:
    """task 9"""
    return [(i, len(i)) for i in lst]
