#!/usr/bin/env python3
"""task 0"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """async function that wait for a random number between 0 nas max_delay"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
