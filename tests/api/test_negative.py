import requests

from utils import api_client
from utils.api_client import BASE_URL
from utils.test_data import booking_missing_required


def test_bad_auth_credentials():
    resp = requests.post(
        f"{BASE_URL}/auth",
        json={"username": "no", "password": "no"},
    )
    assert "token" not in resp.json()


def test_update_without_token_is_forbidden():
    resp = requests.put(f"{BASE_URL}/booking/1", json={"firstname": "x"})
    assert resp.status_code == 403


def test_get_nonexistent_booking_is_404():
    resp = api_client.get_booking(99999999)
    assert resp.status_code == 404


def test_create_missing_required_fields_is_rejected():
    # restful-booker does not create a valid booking from an incomplete body
    resp = api_client.create_booking(booking_missing_required())
    assert resp.status_code != 200
