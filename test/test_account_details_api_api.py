# coding: utf-8

"""
    SerpsBot

    Our APIs allow data miners to harvest huge volumes of data from Google and other search engines.  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import serpsbot
from serpsbot.api.account_details_api_api import AccountDetailsAPIApi  # noqa: E501
from serpsbot.rest import ApiException


class TestAccountDetailsAPIApi(unittest.TestCase):
    """AccountDetailsAPIApi unit test stubs"""

    def setUp(self):
        self.api = AccountDetailsAPIApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_account_details_account_info_get(self):
        """Test case for get_account_details_account_info_get

        Get Account Details  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
