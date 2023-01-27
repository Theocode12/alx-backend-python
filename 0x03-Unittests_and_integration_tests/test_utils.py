#!/usr/bin/env python3
"""Tests for utils module"""
from unittest import TestCase, main
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import memoize
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

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False}),
        ]
    )
    def test_get_json(self, test_url, test_payload):
        """
        Tests if the mocked get method was calles once
        Tests if the output is equal to the payload
        """
        mock_resp = Mock()
        mock_resp.json.return_value = test_payload
        with patch("utils.requests.get") as mock_request:
            mock_request.return_value = mock_resp
            payload = utils.get_json(test_url)
            self.assertEqual(payload, test_payload)
            mock_request.assert_called_once()


class TestMemoize(TestCase):
    """Tests memoized decorator"""

    def test_memoize(self):
        """unittest for memoize"""

        class TestClass:
            """Our test class"""

            def a_method(self):
                """Method to mock"""
                return 42

            @memoize
            def a_property(self):
                """memoized function"""
                return self.a_method()

        with patch.object(TestClass, "a_method") as mock_method:
            mock_method.return_value = 42
            my_object = TestClass()
            res1, res2 = my_object.a_property, my_object.a_property
            self.assertEqual(res1, res2)
            mock_method.assert_called_once()


if __name__ == "__main__":
    main()
