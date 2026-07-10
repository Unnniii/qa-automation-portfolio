import requests

from utils.api_client import BASE_URL


def test_auth_returns_token(api_token):
    assert api_token  # session fixture already asserted 200 via raise_for_status


def test_auth_bad_credentials():
    resp = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "bad", "password": "bad"},
    )
    assert "token" not in resp.json()
