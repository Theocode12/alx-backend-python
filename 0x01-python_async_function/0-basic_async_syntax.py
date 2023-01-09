#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait for a random number of seconds(float)"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
