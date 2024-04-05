from app import app


# These unit checks are somewhat fragile as test.db could be wiped or content changed.
# TODO generate test db before each run
# If this was a production app more coverage than happy path and some negative checks would be appropriate


def test_get_all_messages():
    response = app.test_client().get("/message/all")
    assert response.status_code == 200
    assert response.data is not None


def test_get_messages():
    response = app.test_client().get("/message/1")
    assert response.status_code == 200
    assert response.data is not None


def test_get_nonexistent_messages():
    response = app.test_client().get("/message/9999")
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Invalid message id"


def test_get_invalid_message_id():
    response = app.test_client().get("/message/yes")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Invalid message id, must be a number"


def test_create_message():
    response = app.test_client().post("/message", json={"message": "here's one"})
    assert response.status_code == 200
    assert response.data is not None


def test_create_invalid_message():
    response = app.test_client().post("/message", json={"messages": "here's one"})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Body should be JSON in the schema of {message: messageValue}"


def test_update_message():
    response = app.test_client().put("/message/1", json={"message": "updated"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Message updated"


def test_invalid_update_message():
    response = app.test_client().put("/message/99999", json={"message": "updated"})
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Invalid message id"

def test_invalid_delete_message():
    response = app.test_client().delete("/message/99999")
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Invalid message id"