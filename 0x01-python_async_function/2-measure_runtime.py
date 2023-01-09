#!/usr/bin/env python3
"""A module to illustrate the asynchronous io"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """measures the total time to wait for wait_n"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = time.perf_counter() - start
    return stop / n
