#!/usr/bin/env python3
"""task 8"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """task 8"""
    def muliply(value: float) -> float:
        """task 8"""
        return value * multiplier
    return muliply
