#!/usr/bin/env python3
"""task 1"""
import asyncio
from typing import List


wait_random: float = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """task 1"""
    ls = []
    for i in range(n):
        delay = await wait_random(max_delay)
        ls.append(delay)
    return ls
