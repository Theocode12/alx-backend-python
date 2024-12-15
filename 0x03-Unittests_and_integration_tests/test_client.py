#!/usr/bin/env python3
""" Unittest with parametarize  """

from parameterized import parameterized, parameterized_class
import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestGithubOrgClient(unittest.TestCase):
    """mocks utils.get_json function and tests github client"""

    @parameterized.expand(
        [
            ("google", {"repos_url": "github.com/google"}),
            ("abc", {"repos_url": "github.com/abc_repo"}),
        ]
    )
    @patch("requests.get")
    def test_org(
            self, org: str, response: Mapping, mocked_get: Any
    ):
        """mocks request.get to test getting json from an api"""
        mock_response = MagicMock()
        mock_response.json.return_value = response
        mocked_get.return_value = mock_response
        gh_client = GithubOrgClient(org)
        resp_from_gh_client = gh_client.org
        self.assertEqual(resp_from_gh_client, response)
        mocked_get.assert_called_once_with(gh_client.ORG_URL.format(org=org))

    def test_public_repos_url(self):
        """mocks request.get to test getting json from an api"""
        gh_client = GithubOrgClient("google")
        with patch(
             "client.GithubOrgClient.org", new_callable=PropertyMock
        ) as mocked_method:
            mocked_method.return_value = {"repos_url": "github.com/google"}
            resp_from_gh_client = gh_client._public_repos_url
            self.assertEqual(resp_from_gh_client, "github.com/google")