#!/usr/bin/env python3
"""
asyncio.Task
"""
import asyncio
import random


async def wait_random(max_delay: int) -> float:
    """
    asynchronous function that waits for a
    random amount of time between 0 and max_delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    create an asyncio.Task that wraps the wait_random function
    """
    return asyncio.create_task(wait_random(max_delay))


async def test(max_delay: int) -> None:
    task = task_wait_random(max_delay)
    await task
    print(task.__class__)


asyncio.run(test(5))
