#!/usr/bin/env python3
"""A module that shows basic annotations"""

from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Basic annotation"""
    if lst:
        return lst[0]
    else:
        return None
