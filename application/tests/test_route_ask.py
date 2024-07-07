from typing import Generator

from flask import Flask
from flask.testing import FlaskClient
import pytest
from unittest.mock import patch

from application import application

@pytest.fixture
def app() -> Generator[Flask, None, None]:
    app: Flask = application
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql:///:memory:",
    })

    with app.app_context():
        with patch('application.db.session'):
            yield app

@pytest.fixture
def client(app: Flask) -> FlaskClient:
    return app.test_client()

def test_get_chats_success(client: FlaskClient) -> None:
    question: str = "How are you?"
    response = client.post('/ask', json={"question": question})
    json_data = response.get_json()

    assert response.status_code == 201
    assert json_data["question"] == question

def test_get_chats_no_question(client: FlaskClient) -> None:
    response = client.post('/ask', json={})
    json_data = response.get_json()

    assert response.status_code == 400
    assert json_data["error"] == "The 'question' field is required."
