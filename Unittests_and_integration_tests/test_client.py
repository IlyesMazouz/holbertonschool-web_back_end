#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class for testing the GithubOrgClient class.
    """

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    @patch("client.GithubOrgClient.get_json")
    def test_has_license(self, repo, license_key, expected_result, mock_get_json):
        """
        Test that has_license returns the expected
        result based on the repository's license.
        """
        mock_get_json.return_value = [repo]

        client = GithubOrgClient("org_name")

        has_license = client.has_license(license_key)

        self.assertEqual(has_license, expected_result)

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/org_name/repos"
        )
