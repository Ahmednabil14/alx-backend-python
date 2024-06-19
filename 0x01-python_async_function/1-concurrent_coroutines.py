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
    print(ls)
    sorted_list = []
    for item in ls:
        flag = False
        for i in sorted_list:
            if item < i:
                sorted_list.insert(sorted_list.index(i), item)
                flag = True
                break
        if not flag:
            sorted_list.append(item)
    return sorted_list
