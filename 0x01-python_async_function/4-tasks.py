#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """return the list of all the delays (float values)"""
    return sorted(await asyncio.gather(*(task_wait_random(max_delay)
                                         for _ in range(n))))
