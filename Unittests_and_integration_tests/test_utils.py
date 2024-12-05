#!/usr/bin/env python3
"""
Unit tests for utils.memoize.
"""

import unittest
from unittest.mock import patch, MagicMock
from utils import memoize


class TestMemoize(unittest.TestCase):
    """
    TestMemoize class for testing the memoize decorator.
    """

    def test_memoize(self):
        """
        Test the memoize decorator.
        """

        class TestClass:
            """
            A test class to validate the memoize decorator.
            """

            def a_method(self):
                """
                A method that returns a constant value.
                """
                return 42

            @memoize
            def a_property(self):
                """
                A memoized property that calls a_method.
                """
                return self.a_method()

        patcher = patch.object(TestClass, "a_method", return_value=42)
        with patcher as mock_method:
            test_instance = TestClass()

            self.assertEqual(test_instance.a_property, 42)

            self.assertEqual(test_instance.a_property, 42)

            mock_method.assert_called_once()
