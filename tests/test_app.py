import pytest
import sys
import os

from app.app import app  # Importing your Flask application

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

@pytest.fixture
def client():
    # Create a test client for the Flask application
    with app.test_client() as client:
        yield client

def test_homepage(client):
    # Test the homepage route
    response = client.get('/')
    assert response.status_code == 200  # Expecting a 200 OK response
    assert b'Hello, Flask!' in response.data  # Verifying the expected content
