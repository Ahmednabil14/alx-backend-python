#!/usr/bin/env python3
"""task 4"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    ls = []
    for i in range(n):
        delay = await task_wait_random(max_delay)
        ls.append(delay)
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
