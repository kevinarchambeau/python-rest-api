# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestMessageController(BaseTestCase):
    """MessageController integration test stubs"""

    def test_message_all_get(self):
        """Test case for message_all_get

        Get all messages
        """
        response = self.client.open(
            '//message/all',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_message_id_delete(self):
        """Test case for message_message_id_delete

        Deletes a message
        """
        response = self.client.open(
            '//message/{messageId}'.format(message_id=Object()),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_message_id_get(self):
        """Test case for message_message_id_get

        Find message by ID
        """
        response = self.client.open(
            '//message/{messageId}'.format(message_id=Object()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_message_id_put(self):
        """Test case for message_message_id_put

        Update a message by ID
        """
        response = self.client.open(
            '//message/{messageId}'.format(message_id=Object()),
            method='PUT')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_message_post(self):
        """Test case for message_post

        Adds a message
        """
        response = self.client.open(
            '//message',
            method='POST')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
