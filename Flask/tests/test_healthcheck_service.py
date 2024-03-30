import json
import pytest
from app import app
from flask import Flask, Response
from flask.testing import FlaskClient


@pytest.fixture
def client(request) -> FlaskClient:
    # Instantiate test client
    test_client: FlaskClient = app.test_client()

    # This is a placeholder to define teardown for test cleanup
    def teardown() -> None:
        pass
    request.addfinalizer(teardown)
    return test_client


def test_service_status(client: FlaskClient) -> None:
    # Make a get call
    response: Response = client.get('/healthcheck')
    # Validate get call returns 200
    assert response.status_code == 200
    # assert b'service_status' in response.data
