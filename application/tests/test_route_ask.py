import pytest
from unittest.mock import patch
from application import application

@pytest.fixture
def app():
    app = application
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql:///:memory:",
    })

    with app.app_context():
        with patch('application.db.session'):
            yield app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_chats_success(client):
    question = "How are you?"
    response = client.post('/ask', json={"question": question})
    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data["question"] == question

def test_get_chats_no_question(client):
    response = client.post('/ask', json={})
    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data["error"] == "A question must be in the request."
