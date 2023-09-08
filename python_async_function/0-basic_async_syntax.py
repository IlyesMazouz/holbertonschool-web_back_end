#!/usr/bin/env python3
"""
delay function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    returns the delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
