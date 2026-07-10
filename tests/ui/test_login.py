import pytest

from pages.login_page import LoginPage


def test_valid_login(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "secret_sauce")
    assert "inventory.html" in page.url


def test_invalid_password(page):
    login = LoginPage(page)
    login.load()
    login.login("standard_user", "wrong_password")
    assert "Username and password do not match" in login.error_message()


def test_locked_out_user(page):
    login = LoginPage(page)
    login.load()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.error_message()


@pytest.mark.parametrize(
    "username,password",
    [
        ("", "secret_sauce"),
        ("standard_user", ""),
        ("bad_user", "bad_pass"),
    ],
)
def test_invalid_logins(page, username, password):
    login = LoginPage(page)
    login.load()
    login.login(username, password)
    assert login.error_message()  # any error banner means login was rejected
