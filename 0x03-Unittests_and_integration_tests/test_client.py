#!/usr/bin/env python3
"""Test GithubOrgClient org method"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google", {"repos_url": "https://api.github.com/orgs/google/repos"}),
        ("abc", {"repos_url": "https://api.github.com/orgs/abc/repos"})
    ])
    @patch('client.get_json', return_value={"repos_url": "mock_url"})
    def test_org(self, org_name, expected, mock_get_json):
        """Test org method"""

        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, {"repos_url": "mock_url"})
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )


if __name__ == '__main__':
    unittest.main()
