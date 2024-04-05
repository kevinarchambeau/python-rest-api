from flask import Flask, Response, request
from db import SQLite
import numbers
import jwt
import configparser
import time
import requests
import os

app = Flask(__name__)

DB_NAME = os.getenv("DB_PATH", default="/app/demodb.db")
print(DB_NAME)
config = configparser.ConfigParser()
config_file = os.getenv("CONFIG_FILE", default="/app/conf/appConfig.ini")
print(config_file)
config.read(config_file)
# App config for jwt endpoints
jwt_conf = config["JWT"]
JWT_ALGO = jwt_conf.get("algorithm")
JWT_KEY = jwt_conf.get("key")
JWT_ISSUER = jwt_conf.get("valid_issuer")
JWT_TTL = int(jwt_conf.get("ttl"))


@app.route("/message/all", methods=["GET"])
def get_all_messages():
    # This endpoint shouldn't exist in a production app as is, at a minimum page pagination should be used
    # TODO use connection pooling
    db = SQLite(DB_NAME)
    messages = db.get_all_messages()
    db.close()

    if not messages:
        return Response("Unable to retrieve messages", 500)

    return messages


@app.route("/message", methods=["POST"])
def insert_messages():
    body = request.json
    message = body.get('message')

    if not message or not is_string(message):
        return Response('Body should be JSON in the schema of {"message": "messageValue"}', 400)

    db = SQLite(DB_NAME)
    message_id = str(db.insert_message(message))
    if not message_id:
        db.close()
        return Response("Insert failed", 500)

    response = db.get_messages(message_id)
    db.close()

    return response


@app.route("/message/<message_id>", methods=["GET"])
def get_messages(message_id):
    if not is_num(message_id):
        return Response("Invalid message id, must be a number", 400)

    db = SQLite(DB_NAME)
    message = db.get_messages(message_id)
    db.close()

    if not message:
        return Response("Invalid message id", 404)

    return message


@app.route("/message/<message_id>", methods=["DELETE"])
def delete_messages(message_id):
    if not is_num(message_id):
        return Response("Invalid message id, must be a number", 400)

    db = SQLite(DB_NAME)
    exists = db.get_messages(message_id)

    if not exists:
        db.close()
        return Response("Invalid message id", 404)

    result = db.delete_message(message_id)
    db.close()

    if not result:
        return Response("Message could not be deleted", 500)

    return Response("Message deleted")


@app.route("/message/<message_id>", methods=["PUT"])
def update_messages(message_id):
    if not is_num(message_id):
        return Response("Invalid message id, must be a number", 400)

    body = request.json
    message = body.get('message')
    if not message or not is_string(message):
        return Response('Body should be JSON in the schema of {"message": "messageValue"}', 400)

    db = SQLite(DB_NAME)
    exists = db.get_messages(message_id)

    if not exists:
        db.close()
        return Response("Invalid message id", 404)

    result = db.update_message(message_id, message)
    if not result:
        return Response("Message not updated", 500)
    db.close()

    return Response("Message updated")


@app.route("/jwt/build", methods=["GET"])
def create_jwt():
    issuer = request.args.get("issuer", default="anonymous")
    subject = request.args.get("subject", default="anonymous")
    expiration = int(time.time()) + JWT_TTL
    payload = {
        "iss": issuer,
        "sub": subject,
        "nbf": expiration - JWT_TTL,
        "exp": expiration
    }
    encoded = jwt.encode(payload, JWT_KEY, JWT_ALGO)

    return encoded


@app.route("/jwt/validate", methods=["GET"])
def validate_jwt():
    bearer = request.headers.get("Authorization")
    if not bearer:
        return Response("No valid auth header present", 400)
    try:
        token = bearer.split()[1]
    except Exception:
        return Response("No valid auth header present", 400)

    try:
        decoded = jwt.decode(token, JWT_KEY, JWT_ALGO)
    except (jwt.ExpiredSignatureError, jwt.DecodeError):
        return Response("Invalid token", 400)

    if decoded.get("iss") != JWT_ISSUER:
        return Response("Invalid token", 400)

    return "Token is valid"


@app.route("/richandmorty/character", methods=["GET"])
def get_characters():
    response = requests.get("https://rickandmortyapi.com/api/character")
    if response.status_code == 200:
        return response.text
    else:
        return Response(f"Error occurred with external API: {response.status_code} : {response.text} ", 400)


@app.route("/richandmorty/character/<character_id>", methods=["GET"])
def get_character(character_id):
    response = requests.get(f"https://rickandmortyapi.com/api/character/{character_id}")
    if response.status_code == 200:
        return response.text
    else:
        return Response(f"Error occurred with external API: {response.status_code} : {response.text} ", 400)


# Helper functions to improve readability
def is_num(value):
    try:
        isinstance(int(value), numbers.Number)
    except Exception:
        return False

    return True


def is_string(value):
    return isinstance(value, str)
