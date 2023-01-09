#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> list:
    """return the list of all the delays (float values)"""
    return sorted(await asyncio.gather(*(wait_random(max_delay)
                                         for _ in range(n))))
