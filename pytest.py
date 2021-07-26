import pytest
from app import create_app as app



@pytest.fixture
def app():
    yield app


@pytest.fixture
def client(app):
    return app.test_client()



def test_index(app, client):
    res = client.get('/')
    assert res.status_code == 200       #expect an output without errors
    