#!/usr/bin/env python3
"""Basic Annotations"""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Basic Annotations"""
    if key in dct:
        return dct[key]
    else:
        return default
