#!/usr/bin/env python3
""" Unittest with parametarize  """

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, MagicMock
from utils import access_nested_map, get_json, memoize
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Tests utils.access_nested_map"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(
        self, nested_map: Mapping, keys: Sequence, value: Any
    ):
        """tests valid path"""
        self.assertEqual(access_nested_map(nested_map, keys), value)

    @parameterized.expand(
        [
            ("attempts to access empty map", {}, ("a",)),
            ("attempts to access a non existent map", {"a": 1}, ("a", "b")),
        ]
    )
    def test_access_nested_map_exception(
        self, name: str, nested_map: Mapping, keys: Sequence
    ):
        """tests invalid path"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(nested_map, keys)


class TestGetJson(unittest.TestCase):
    """mocks utils.get_json function"""

    @parameterized.expand(
        [
            ("example url", "http://example.com", {"payload": True}),
            ("holbertom url", "http://holberton.io", {"payload": False}),
        ]
    )
    @patch("requests.get")
    def test_get_json(
            self, name: str, url: str, response: Mapping, mocked_get: Any
    ):
        """mocks request.get to test getting json from an api"""
        mock_response = MagicMock()
        mock_response.json.return_value = response
        mocked_get.return_value = mock_response
        self.assertEqual(get_json(url), response)
        mocked_get.assert_called_once_with(url)


class TestMemoize(unittest.TestCase):
    """tests utils.memoize"""

    def test_memoize(self):
        """tests test_memoize"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        testClassInstance = TestClass()
        with patch.object(testClassInstance, "a_method") as mocked_method:
            mocked_method.return_value = 42
            self.assertEqual(testClassInstance.a_property, 42)
            self.assertEqual(testClassInstance.a_property, 42)
            mocked_method.assert_called_once()
