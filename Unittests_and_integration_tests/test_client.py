#!/usr/bin/env python3
""" Test the GithubOrgClient """
import unittest
from unittest.mock import patch
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
