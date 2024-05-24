import pytest
from flask_api.app import app as api


@pytest.fixture()
def app():
    app = api
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()


def test_request_example(client):
    response = client.get("/coffee")
    assert "Let's make some tea!" in str(response.data)
    assert 418 == response.status_code
