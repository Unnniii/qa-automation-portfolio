import pytest
import requests

from pages.login_page import LoginPage

API_BASE = "https://restful-booker.herokuapp.com"


@pytest.fixture
def logged_in_page(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    return page


@pytest.fixture(scope="session")
def api_token():
    resp = requests.post(
        f"{API_BASE}/auth",
        json={"username": "admin", "password": "password123"},
    )
    resp.raise_for_status()
    return resp.json()["token"]
