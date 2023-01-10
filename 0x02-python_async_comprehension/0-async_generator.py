#!/usr/bin/env python3
"""A module that implements the use of async generators"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates a random number from 0-10"""

    for n in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
