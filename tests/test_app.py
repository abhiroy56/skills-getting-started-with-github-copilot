import pytest


def test_root_redirect(client):
    """Test that root endpoint redirects to static files"""
    response = client.get("/", follow_redirects=False)
    assert response.status_code == 307
    assert response.headers["location"] == "/static/index.html"


def test_get_activities(client):
    """Test retrieving all activities"""
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    
    # Verify we have activities
    assert isinstance(data, dict)
    assert len(data) > 0
    
    # Verify structure of an activity
    for activity_name, activity_data in data.items():
        assert "description" in activity_data
        assert "schedule" in activity_data
        assert "max_participants" in activity_data
        assert "participants" in activity_data
