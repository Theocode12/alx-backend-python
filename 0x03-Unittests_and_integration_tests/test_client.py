#!/usr/bin/env python3
"""Tests the client module"""
from unittest import TestCase
from unittest.mock import patch, PropertyMock, Mock, MagicMock
from client import GithubOrgClient
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD

class TestGithubOrgClient(TestCase):
    """Test Github API client"""

    @parameterized.expand([("google"), ("abc")])
    @patch("client.get_json")
    def test_org(self, org, mock_json):
        """"""
        github = GithubOrgClient(org)
        github.org
        mock_json.assert_called_once()

    @parameterized.expand([("google"), ("abc")])
    def test_public_repos_url(self, org_name):
        """Test _public_repos_url from GithubOrgClient"""
        payload = {
            "repos_url": "https://api.github.com/orgs/{}/repos".format(
                org_name
            )
        }
        git_org = GithubOrgClient(org_name)
        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
            return_value=payload,
        ) as MockClient:
            self.assertEqual(git_org._public_repos_url, payload["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock_json):
        """Test GithubOrgClient.public_repos method"""
        mock_json.return_value = [
            {"name": "projectA"},
            {"name": "projectB"},
            {"name": "projectC"},
        ]
        # git_org = GithubOrgClient(org_name)
        with patch(
            "client.GithubOrgClient._public_repos_url",
            new_callable=PropertyMock,
        ) as mock_pub_repos:
            mock_pub_repos.return_value = "https://api.github.com/orgs/repos"
            # pub_repo = git_org.public_repos()
            # repos = [repo["name"] for repo in mock_json.return_value]
            # self.assertListEqual(repos, pub_repo)
            # mock_json.assert_called_once()

    @parameterized.expand(
        [
            ({"license": {"key": "my_license"}}, "my_license", True),
            ({"license": {"key": "other_license"}}, "my_license", False),
        ]
    )
    def test_has_license(self, repo, license_key, h_license):
        """Test if liense is available"""
        self.assertEqual(
            GithubOrgClient.has_license(repo, license_key), h_license
        )

@parameterized_class(('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'))
class TestIntegrationGithubOrgClient(TestCase):
    """Integration tests for public_repos"""
    def setUp(self) -> None:
        resp = MagicMock(json=MagicMock(side_effect=TEST_PAYLOAD))
        self.get_patcher= patch("client.get_json", return_value=resp)
        self.get_patcher.start()
        
        
    def tearDownClass(self) -> None:
        self.get_patcher.stop()
        return super().tearDown()