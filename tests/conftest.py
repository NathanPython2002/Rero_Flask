import pytest
from app import create_app

@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app = create_app()
    app.testing = True
    return app.test_client()