from flask import Flask, Response, request
from db import SQLite
import numbers

app = Flask(__name__)


@app.route("/message/all", methods=['GET'])
def get_all_messages():
    # This endpoint shouldn't exist in a production app as is, at a minimum page pagination should be used
    db = SQLite()
    messages = db.get_all_messages()
    db.close()
    return messages


@app.route("/message", methods=['POST'])
def insert_messages():
    body = request.json
    message = body.get('message')
    if not message:
        return Response("Body should be JSON in the format of id:message", 400)
    db = SQLite()
    message_id = db.insert_message(message)

    return {message_id: message}


@app.route("/message/<message_id>", methods=['GET'])
def get_messages(message_id):
    if not isinstance(message_id, numbers.Number):
        return Response("Invalid message id, must be a number", 400)

    db = SQLite()
    message = db.get_messages(message_id)
    db.close()
    if not message:
        return Response("Invalid message id", 404)

    return message


@app.route("/message/<message_id>", methods=['DELETE'])
def delete_messages(message_id):
    if not isinstance(message_id, numbers.Number):
        return Response("Invalid message id, must be a number", 400)

    return {
        "id": message_id,
        "delete": "yes"
    }


@app.route("/message/<message_id>", methods=['PUT'])
def update_messages(message_id):
    if not isinstance(message_id, numbers.Number):
        return Response("Invalid message id, must be a number", 400)

    return {
        "id": message_id,
        "put": "yes"
    }
