#!/usr/bin/env python3
"""
a synchronous coroutine that waits for a random delay between 0 and max_delay
(inclusive) secondsand returns the delay as a float
"""

import asyncio
import random
from typing import List
from concurrent.futures import FIRST_COMPLETED


async def wait_random(max_delay: int = 10) -> float:
    """
    randome delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    randome delay
    """
    delays = []

    async def wait_random_and_append():
        nonlocal delays
        delay = await wait_random(max_delay)
        delays.append(delay)

    tasks = [wait_random_and_append() for _ in range(n)]

    while tasks:
        done, tasks = await asyncio.wait(tasks, return_when=FIRST_COMPLETED)

    return sorted(delays)
