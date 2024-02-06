#!/usr/bin/env python3
"""
Define a test class to test functions in
utils module.
"""
from unittest import TestCase
from unittest.mock import (
        patch,
        Mock
        )
from parameterized import parameterized
from utils import access_nested_map
from utils import get_json


class TestAccessNestedMap(TestCase):
    """
    Test class for the access nested map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access nested map function. """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a", )),
        ({"a": 1}, ("a", "b", )),
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access nested map function with
        exceptions.
        """
        with self.assertRaises(KeyError):
            self.assertEqual(access_nested_map(nested_map, path), expected)


class TestGetJson(TestCase):
    """
    Test class for the get json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
        ])
    def test_get_json(self, url, payload):
        """ Test get json function. """
        mock = Mock()
        mock.json.return_value = payload

        with patch("requests.get", return_value=mock) as magic_mock:
            response = get_json(url)
            magic_mock.assert_called_once_with(url)
            self.assertEqual(response, payload)
