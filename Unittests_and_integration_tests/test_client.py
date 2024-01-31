#!/usr/bin/env python3
""" Test the GithubOrgClient """
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """
        Test the GithubOrgClient
    """

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch("client.get_json")
    def test_org(self, provider, mock_get_json):
        """ test GithubOrgClient.org by patching get_json"""
        mock_get_json.return_value = {"provider": provider}
        gh_client = GithubOrgClient("google")
        self.assertEqual(gh_client.org, {"provider": provider})
        mock_get_json.assert_called_once()

    @patch("client.GithubOrgClient.org", new_callable=PropertyMock)
    def test_public_repos_url(self, mock_public_repos_url):
        """
            Make sure that GithubOrgClient._public_repos_url works properly
        """
        mock_public_repos_url.return_value = {"repos_url": "test"}
        gh_client = GithubOrgClient("asdf")
        self.assertEqual(gh_client._public_repos_url, "test")

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """ Test public_repos """
        test_repos = [
            {"name": "numberone", "license": {"key": "ABC123"}},
            {"name": "numbertwo", "license": {"key": "OPENSESAME"}},
        ]
        test_names = ["numberone", "numbertwo"]
        mock_get_json.return_value = test_repos
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://www.internet.com"
            gh_client = GithubOrgClient("fweio")
            pub_repo_names = gh_client.public_repos()
            self.assertEqual(pub_repo_names, test_names)
            mock_get_json.assert_called_once_with("https://www.internet.com")
            mock_public_repos_url.assert_called_once()
