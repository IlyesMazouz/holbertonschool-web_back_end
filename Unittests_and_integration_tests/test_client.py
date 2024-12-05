#!/usr/bin/env python3
"""
Integration tests for client.GithubOrgClient.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized_class
import requests
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos


@parameterized_class(
    [
        {
            "org_payload": org_payload,
            "repos_payload": repos_payload,
            "expected_repos": expected_repos,
            "apache2_repos": apache2_repos,
        }
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """
    Integration test for GithubOrgClient.public_repos method, with external requests mocked.
    """

    @classmethod
    def setUpClass(cls):
        """
        Set up class method to mock requests.get and return mock data for testing.
        """
        cls.get_patcher = patch("requests.get")
        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = cls.mock_requests_get

    @classmethod
    def tearDownClass(cls):
        """
        Tear down class method to stop the patcher after tests are run.
        """
        cls.get_patcher.stop()

    @staticmethod
    def mock_requests_get(url, *args, **kwargs):
        """
        Side effect function for mocking requests.get calls.
        It will return different payloads based on the URL.
        """
        if url == "https://api.github.com/orgs/org_name":
            return MockResponse(org_payload)
        elif url == "https://api.github.com/orgs/org_name/repos":
            return MockResponse(repos_payload)
        else:
            raise ValueError(f"Unexpected URL: {url}")

    def test_public_repos(self):
        """
        Test that the public_repos method returns the expected list of repos.
        """
        client = GithubOrgClient("org_name")
        repos = client.public_repos()

        self.assertEqual(repos, expected_repos)

        self.mock_get.assert_called_with("https://api.github.com/orgs/org_name")
        self.mock_get.assert_called_with("https://api.github.com/orgs/org_name/repos")


class MockResponse:
    """
    Mock class for simulating a Response object returned by requests.get().
    It provides a json() method that returns the mock payload.
    """

    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data
