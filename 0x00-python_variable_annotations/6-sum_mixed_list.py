#!/usr/bin/env python3
"""A module that shows basic annotations"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of ints or floats"""
    return sum(mxd_lst)
