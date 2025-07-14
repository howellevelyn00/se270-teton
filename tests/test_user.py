import requests
import pytest

BASE_URL = "https://127.0.0.1:8000/users"
VERIFY_SSL = False  # skip SSL verification for localhost dev testing


def test_unauthorized_users_endpoint():
    """Should return 401 with an empty plain text response for bad credentials"""
    params = {
        "username": "admin",
        "password": "admin"
    }

    response = requests.get(BASE_URL, params=params, verify=VERIFY_SSL)

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.headers.get("Content-Type", "").startswith("text"), \
        f"Expected text response, got: {response.headers.get('Content-Type')}"
    assert response.text.strip() == "", f"Expected empty response body, got: {response.text!r}"


def test_authorized_users_endpoint_empty_response():
    """Should return 200 with an empty plain text response for valid credentials"""
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    response = requests.get(BASE_URL, params=params, verify=VERIFY_SSL)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.headers.get("Content-Type", "").startswith("text"), \
        f"Expected text response, got: {response.headers.get('Content-Type')}"
    assert response.text.strip() == "", f"Expected empty response body, got: {response.text!r}"
