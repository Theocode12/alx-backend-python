#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> list:
    """return the list of all the delays (float values)"""
    return [await task_wait_random(max_delay) for i in range(n)]
