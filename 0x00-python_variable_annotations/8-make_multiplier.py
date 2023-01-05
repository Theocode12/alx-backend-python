#!/usr/bin/env python3
"""A module that shows basic annotations"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""

    return lambda x: x * multiplier
