import pytest
import os
from hdi_app import create_app, db

@pytest.fixture
def app():
    """Create and configure a new app instance for each test."""
    os.environ['FLASK_CONFIG'] = 'development'
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"
    })

    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

def test_home_page(client):
    """Test that the home page loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b"A Comprehensive Measure of Well-Being" in response.data

def test_login_page(client):
    """Test that the login page loads."""
    response = client.get('/login')
    assert response.status_code == 200
    assert b"Welcome Back" in response.data

def test_predict_requires_login(client):
    """Test that predicting requires authentication."""
    response = client.get('/predict')
    # Should redirect to login page (302)
    assert response.status_code == 302
    assert b"/login" in response.data
