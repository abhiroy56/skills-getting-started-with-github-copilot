import pytest


def test_signup_for_activity_success(client, sample_email):
    """Test successful signup for an activity"""
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": sample_email}
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert sample_email in data["message"]


def test_signup_activity_not_found(client, sample_email):
    """Test signup fails when activity doesn't exist"""
    response = client.post(
        "/activities/Nonexistent Activity/signup",
        params={"email": sample_email}
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_signup_already_registered(client):
    """Test signup fails when student is already registered"""
    email = "michael@mergington.edu"  # Already in Chess Club
    response = client.post(
        "/activities/Chess Club/signup",
        params={"email": email}
    )
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_remove_participant_success(client):
    """Test successful removal of participant"""
    email = "michael@mergington.edu"  # Participant in Chess Club
    response = client.delete(
        f"/activities/Chess Club/participants/{email}"
    )
    assert response.status_code == 200
    assert "message" in response.json()


def test_remove_participant_activity_not_found(client):
    """Test removal fails when activity doesn't exist"""
    response = client.delete(
        "/activities/Nonexistent/participants/test@example.com"
    )
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_remove_participant_not_signed_up(client):
    """Test removal fails when student isn't signed up"""
    email = "notsignedup@mergington.edu"  # Email that's definitely not signed up
    response = client.delete(
        f"/activities/Chess Club/participants/{email}"
    )
    assert response.status_code == 404
    assert "not signed up" in response.json()["detail"]
