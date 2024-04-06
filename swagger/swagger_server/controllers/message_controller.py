import connexion
import six

from swagger_server import util


def message_all_get():  # noqa: E501
    """Get all messages

     # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def message_message_id_delete(message_id):  # noqa: E501
    """Deletes a message

    message a pet # noqa: E501

    :param message_id: ID of message to delete
    :type message_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        message_id = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def message_message_id_get(message_id):  # noqa: E501
    """Find message by ID

    Returns a single message # noqa: E501

    :param message_id: ID of message to return
    :type message_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        message_id = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def message_message_id_put(message_id):  # noqa: E501
    """Update a message by ID

    Body: {\&quot;message\&quot;: \&quot;messageValue\&quot;} # noqa: E501

    :param message_id: ID of message to update
    :type message_id: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        message_id = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def message_post():  # noqa: E501
    """Adds a message

    Body: {\&quot;message\&quot;: \&quot;messageValue\&quot;} # noqa: E501


    :rtype: None
    """
    return 'do some magic!'
