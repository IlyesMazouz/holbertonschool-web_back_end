#!/usr/bin/env python3
"""
Unit tests for utils.access_nested_map.
"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    TestAccessNestedMap class for testing the access_nested_map function.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
        self, nested_map: dict, path: tuple, expected: any
    ):
        """
        Test access_nested_map with various inputs.
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)
