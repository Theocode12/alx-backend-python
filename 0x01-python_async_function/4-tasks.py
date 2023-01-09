#!/usr/bin/env python3

from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List:
    """return the list of all the delays (float values)"""
    return [await task_wait_random(max_delay) for i in range(n)]
