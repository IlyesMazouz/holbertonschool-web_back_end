#!/usr/bin/env python3
"""
Unit tests for utils.get_json.
"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import get_json


class TestGetJson(unittest.TestCase):
    """
    TestGetJson class for testing the get_json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch("utils.requests.get")
    def test_get_json(self, test_url: str, test_payload: dict, mock_get: Mock):
        """
        Test get_json with mocked requests.get.
        """
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        self.assertEqual(get_json(test_url), test_payload)

        mock_get.assert_called_once_with(test_url)

