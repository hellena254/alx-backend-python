#!/usr/bin/env python3
"""
Module for testing utility functions.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """
    Test case for the access_nested_map function in utils module.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Test access_nested_map function with different inputs.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys to navigate through the nested dictionary.
            expected: The expected value returned by the function.

        Asserts:
            The function's return value is equal to the expected value.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Test access_nested_map function raises KeyError for invalid paths.

        Args:
            nested_map (dict): The nested dictionary to access.
            path (tuple): The sequence of keys to navigate through the nested dictionary.

        Asserts:
            The function raises a KeyError with the expected message.
        """
        with self.assertRaises(KeyError) as cm:
            access_nested_map(nested_map, path)
        self.assertEqual(str(cm.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Test case for the get_json function in utils module.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json function with different inputs.

        Args:
            test_url (str): The URL to fetch JSON from.
            test_payload (dict): The expected JSON payload.

        Asserts:
            The mocked get method was called exactly once with test_url.
            The function's return value is equal to test_payload.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json and check the result
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Assert the mocked get method was called once with test_url
        mock_get.assert_called_once_with(test_url)


if __name__ == "__main__":
    unittest.main()
