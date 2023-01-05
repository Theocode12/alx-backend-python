#!/usr/bin/env python3
"""A module that shows basic annotations"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple from k and v"""
    return (k, v*v)
