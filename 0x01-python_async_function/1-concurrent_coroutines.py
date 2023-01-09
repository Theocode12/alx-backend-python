#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""

from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List:
    """return the list of all the delays (float values)"""
    return [await wait_random(max_delay) for i in range(n)]
