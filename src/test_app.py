from app import app, is_num, is_string


# The message unit checks are somewhat fragile as test.db could be wiped or content changed.
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
    assert response.data.decode('utf-8') == 'Body should be JSON in the schema of {"message": "messageValue"}'


def test_update_message():
    response = app.test_client().put("/message/1", json={"message": "updated"})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Message updated"


def test_update_message_invalid():
    response = app.test_client().put("/message/1", json={"message": 33})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Body should be JSON in the schema of {"message": "messageValue"}'


def test_invalid_update_message():
    response = app.test_client().put("/message/99999", json={"message": "updated"})
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Invalid message id"


def test_invalid_delete_message():
    response = app.test_client().delete("/message/99999")
    assert response.status_code == 404
    assert response.data.decode('utf-8') == "Invalid message id"


def test_jwt_default_generation():
    response = app.test_client().get("/jwt/build")
    assert response.status_code == 200
    assert response.data is not None


def test_jwt_with_query_params_generation():
    response = app.test_client().get("/jwt/build?issuer=something&subject=yeah")
    assert response.status_code == 200
    assert response.data is not None


def test_validate_jwt_with_no_header():
    response = app.test_client().get("/jwt/validate")
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "No valid auth header present"


def test_validate_jwt_with_bad_header():
    response = app.test_client().get("/jwt/validate", headers={'Authorization': 'Bearer '})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "No valid auth header present"


def test_validate_jwt_with_bad_token():
    response = app.test_client().get("/jwt/validate", headers={'Authorization': 'Bearer hjrdtdfgqw'})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Invalid token"


def test_validate_jwt_with_expired_token():
    token = ("Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJ4diIsInN1YiI6ImFub255bW91cyIsIm5iZiI6MTcxMjI4Njk3N"
             "ywiZXhwIjoxNzEyMjg3MDM3fQ.HhR7fWiqHEo-Q63F2rr1gwb6z4MfJmgfnHboBeOVp1c")
    response = app.test_client().get("/jwt/validate", headers={'Authorization': token})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Invalid token"


def test_validate_jwt_with_valid_token():
    get_token = app.test_client().get("/jwt/build?issuer=xv")
    token = get_token.data.decode('utf-8')
    response = app.test_client().get("/jwt/validate", headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Token is valid"


def test_validate_jwt_with_invalid_issuer():
    get_token = app.test_client().get("/jwt/build?issuer=something")
    token = get_token.data.decode('utf-8')
    response = app.test_client().get("/jwt/validate", headers={'Authorization': f'Bearer {token}'})
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Invalid token"


# These are integration tests and a bit fragile as the data or contract can change at any time
def test_richandmorty_base():
    response = app.test_client().get("/richandmorty/character")
    assert response.status_code == 200


def test_richandmorty_valid_id():
    response = app.test_client().get("/richandmorty/character/1")
    assert response.status_code == 200
    assert "Rick" in response.data.decode('utf-8')


def test_richandmorty_invalid_id_type():
    response = app.test_client().get("/richandmorty/character/nope")
    assert response.status_code == 400
    assert "500" in response.data.decode('utf-8')


def test_richandmorty_invalid_id():
    response = app.test_client().get("/richandmorty/character/999")
    assert response.status_code == 400
    assert "404" in response.data.decode('utf-8')


def test_is_num():
    assert is_num(13) is True


def test_is_num_string():
    assert is_num([234]) is False


def test_is_string():
    assert is_string("yep a string") is True


def test_is_string_num():
    assert is_string({}) is False
