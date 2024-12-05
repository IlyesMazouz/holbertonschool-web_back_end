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

    @patch("client.GithubOrgClient.get_json")
    @patch.object(
        GithubOrgClient,
        "_public_repos_url",
        return_value="https://api.github.com/orgs/org_name/repos",
    )
    def test_public_repos(self, mock_public_repos_url, mock_get_json):
        """
        Test that public_repos returns the expected list of repos based on the mocked payload.
        """
        mock_get_json.return_value = [{"name": "repo1"}, {"name": "repo2"}]

        client = GithubOrgClient("org_name")

        repos = client.public_repos()

        expected_repos = [{"name": "repo1"}, {"name": "repo2"}]
        self.assertEqual(repos, expected_repos)

        mock_public_repos_url.assert_called_once()

        mock_get_json.assert_called_once_with(
            "https://api.github.com/orgs/org_name/repos"
        )

