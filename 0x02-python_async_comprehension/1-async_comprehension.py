#!/usr/bin/env python3
"""A module that implements the use of async generators"""

from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """use of async generator"""
    return [num async for num in async_generator()]
