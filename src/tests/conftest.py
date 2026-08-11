import pytest
from fastapi.testclient import TestClient

from app import app, activities


@pytest.fixture
def client():
    """Create a test client and reset activity data before each test."""
    original_activities = {
        name: {
            key: (value.copy() if isinstance(value, list) else value)
            for key, value in details.items()
        }
        for name, details in activities.items()
    }

    for activity_name, details in activities.items():
        details["participants"] = list(original_activities[activity_name]["participants"])

    with TestClient(app) as test_client:
        yield test_client

    for activity_name, details in activities.items():
        details["participants"] = list(original_activities[activity_name]["participants"])
