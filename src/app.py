from flask import Flask, Response, request
from db import SQLite
import numbers

app = Flask(__name__)

DB_NAME = "demodb.db"

@app.route("/message/all", methods=['GET'])
def get_all_messages():
    # This endpoint shouldn't exist in a production app as is, at a minimum page pagination should be used
    # TODO use connection pooling
    db = SQLite(DB_NAME)
    messages = db.get_all_messages()
    db.close()

    if not messages:
        return Response("Unable to retrieve messages", 500)

    return messages


@app.route("/message", methods=['POST'])
def insert_messages():
    body = request.json
    message = body.get('message')

    if not message:
        return Response("Body should be JSON in the schema of {message: messageValue}", 400)

    db = SQLite(DB_NAME)
    message_id = str(db.insert_message(message))
    if not message_id:
        db.close()
        return Response("Insert failed", 500)

    response = db.get_messages(message_id)
    db.close()

    return response


@app.route("/message/<message_id>", methods=['GET'])
def get_messages(message_id):
    if not is_num(message_id):
        return Response("Invalid message id, must be a number", 400)

    db = SQLite(DB_NAME)
    message = db.get_messages(message_id)
    db.close()

    if not message:
        return Response("Invalid message id", 404)

    return message


@app.route("/message/<message_id>", methods=['DELETE'])
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


@app.route("/message/<message_id>", methods=['PUT'])
def update_messages(message_id):
    if not is_num(message_id):
        return Response("Invalid message id, must be a number", 400)

    body = request.json
    message = body.get('message')
    if not message:
        return Response("Body should be JSON in the schema of {message: messageValue}", 400)

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


# Helper function to improve readability
def is_num(value):
    try:
        isinstance(int(value), numbers.Number)
    except ValueError:
        return False

    return True
