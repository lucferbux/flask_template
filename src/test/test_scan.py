import os
import tempfile

import pytest

from src import app


@pytest.fixture
def client():
    """Fixture that enables flask in testing mode

    Yields:
        client: Client yielded to use in the following tests
    """
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_insert(client):
    """First test to test the app

    Args:
        client (Flask): Flask applicaiton
    """
    rv = client.post('/api/insert', 
        headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTg0MjIxMjMsIm5iZiI6MTU1ODQyMjEyMywianRpIjoiZTE2ZmFjYzQtZGU4OS00NWY1LWI3MjQtM2YxODM4NjQxZGUwIiwiaWRlbnRpdHkiOiJrX21pdG5pYyIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.BPXKILXs0vDGRRe5svcxlAGJUFMI_gCgX4Y2Xh2B_h0'},
        json=dict(
        author="Juan Gomez Jurado",
        name="Reina Roja",
        year=2018
        ))
    json_data = rv.get_json()
    assert {"200": "OK"} == json_data

def test_empty_bookshelf(client):
    """First test to test the app

    Args:
        client (Flask): Flask applicaiton
    """
    rv = client.get('/api/bookshelf', 
        headers={'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NTg0MjIxMjMsIm5iZiI6MTU1ODQyMjEyMywianRpIjoiZTE2ZmFjYzQtZGU4OS00NWY1LWI3MjQtM2YxODM4NjQxZGUwIiwiaWRlbnRpdHkiOiJrX21pdG5pYyIsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.BPXKILXs0vDGRRe5svcxlAGJUFMI_gCgX4Y2Xh2B_h0'},
    )
    json_data = rv.get_json()
    assert {"200": []} == json_data