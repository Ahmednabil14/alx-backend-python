#!/usr/bin/env python3
"""task 7"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """rertun arguments"""
    return k, v ** 2
