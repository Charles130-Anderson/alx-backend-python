#!/usr/bin/env python3
"""Test GithubOrgClient class"""

import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient class"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test org method returns
        correct value
        """
        expected_return_value = {"login": org_name}
        mock_get_json.return_value = expected_return_value

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_return_value)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos_url(self):
        """Test _public_repos_url method"""
        with patch('client.GithubOrgClient.org',
                   new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/orgs/test/repos"}  
            client = GithubOrgClient("test")
            result = client._public_repos_url

            self.assertEqual(result, "https://api.github.com/orgs/test/repos")


if __name__ == '__main__':
    unittest.main()
