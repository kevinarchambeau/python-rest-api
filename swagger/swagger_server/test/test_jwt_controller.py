# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestJWTController(BaseTestCase):
    """JWTController integration test stubs"""

    def test_jet_build_get(self):
        """Test case for jet_build_get

        Generates a JWT
        """
        query_string = [('issuer', Object()),
                        ('subject', Object())]
        response = self.client.open(
            '//jet/build',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_jwt_validate_get(self):
        """Test case for jwt_validate_get

        Validates token
        """
        headers = [('authorization', Object())]
        response = self.client.open(
            '//jwt/validate',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
