import connexion
import six

from swagger_server import util


def jet_build_get(issuer=None, subject=None):  # noqa: E501
    """Generates a JWT

    Uses default values if issuer or subject aren&#x27;t specified # noqa: E501

    :param issuer: Issuer
    :type issuer: dict | bytes
    :param subject: Subject
    :type subject: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        issuer = Object.from_dict(connexion.request.get_json())  # noqa: E501
    if connexion.request.is_json:
        subject = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def jwt_validate_get(authorization):  # noqa: E501
    """Validates token

     # noqa: E501

    :param authorization: JWT Bearer token
    :type authorization: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        authorization = Object.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
