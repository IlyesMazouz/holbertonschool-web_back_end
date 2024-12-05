#!/usr/bin/env python3
"""
Unit tests for client.GithubOrgClient.
"""

import unittest
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
    TestGithubOrgClient class for testing the GithubOrgClient class.
    """

    def test_public_repos_url(self):
        """
        Test that _public_repos_url returns the
        expected value based on the mocked org.
        """
        with patch.object(
            GithubOrgClient,
            "org",
            return_value={"repos_url": "https://api.github.com/orgs/org_name/repos"},
        ):

            client = GithubOrgClient("org_name")

            repos_url = (
                client._public_repos_url
            )

            expected_url = "https://api.github.com/orgs/org_name/repos"
            self.assertEqual(repos_url, expected_url)

            GithubOrgClient.org.assert_called_once()
