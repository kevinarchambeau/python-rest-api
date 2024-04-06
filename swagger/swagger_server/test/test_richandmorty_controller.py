# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestRichandmortyController(BaseTestCase):
    """RichandmortyController integration test stubs"""

    def test_richandmorty_character_character_id_get(self):
        """Test case for richandmorty_character_character_id_get

        Find character by ID
        """
        response = self.client.open(
            '//richandmorty/character/{characterId}'.format(character_id=Object()),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_richandmorty_character_get(self):
        """Test case for richandmorty_character_get

        Gets all characters
        """
        response = self.client.open(
            '//richandmorty/character',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
