#!/usr/bin/env python3
""" Unittest with parametarize  """

from parameterized import parameterized, parameterized_class
import unittest
from utils import access_nested_map
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """ Tests utils.access_nested_map
    """
    @parameterized.expand([
        ("gets int 1", {"a": 1}, ("a",), 1),
        ("gets dict - {b: 2}", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("gets int  2", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, name: str, nested_map: Mapping, keys: Sequence, value: Any):
        self.assertEqual(access_nested_map(nested_map, keys), value)
