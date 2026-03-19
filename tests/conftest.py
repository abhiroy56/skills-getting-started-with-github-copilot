import pytest
from fastapi.testclient import TestClient
from src.app import app


@pytest.fixture
def client():
    """FastAPI TestClient fixture"""
    return TestClient(app)


@pytest.fixture
def sample_activity():
    """Sample activity data for testing"""
    return {
        "description": "Test Activity",
        "schedule": "Mondays, 3:30 PM - 5:00 PM",
        "max_participants": 20,
        "participants": ["test@example.com"]
    }


@pytest.fixture
def sample_email():
    """Sample email for testing"""
    return "student@mergington.edu"
