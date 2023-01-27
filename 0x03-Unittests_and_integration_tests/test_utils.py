#!/usr/bin/env python3
"""Tests for utils module"""
from unittest import TestCase, main
from unittest.mock import patch
from parameterized import parameterized
import utils

class TestAccessNestedMap(TestCase):
    """Tests class for AccessNestedMap"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
        ]
    )
    def test_access_nested_map(self, nested_map, path, result):
        """Test if the output is correct for a correct input"""
        self.assertEqual(utils.access_nested_map(nested_map, path), result)

    @parameterized.expand([({}, ("a",)), ({"a": 1}, ("a", "b"))])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test if an exception is raised when input is wrong"""
        with self.assertRaises(KeyError):
            utils.access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """Test the get_json method"""
    
    @parameterized.expand([("http://example.com", {"payload": True}),
                           ("http://holberton.io", {"payload": False})])
    def test_get_json(self, test_url, test_payload):
        """
        Tests if the mocked get method was calles once
        Tests if the output is equal to the payload
        """
        with patch('utils.requests.get') as mock_request:
            mock_request.json.return_value = test_payload
            payload = utils.get_json(test_url)
            self.assertEqual(payload, test_payload)
            mock_request.assert_called_once()

if __name__ == "__main__":
    main()
