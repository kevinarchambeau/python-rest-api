import connexion
import six

from swagger_server import util


def richandmorty_character_character_id_get(character_id):  # noqa: E501
    """Find character by ID

    Returns a single character # noqa: E501

    :param character_id: ID of character to return
    :type character_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        character_id = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def richandmorty_character_get():  # noqa: E501
    """Gets all characters

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
