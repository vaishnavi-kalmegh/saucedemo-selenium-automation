import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.smoke
@pytest.mark.login
def test_valid_login(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login(
        credentials["username"], credentials["password"]
    )
    assert InventoryPage(driver).is_loaded()


@pytest.mark.regression
@pytest.mark.login
@pytest.mark.parametrize(
    "username,password,expected",
    [
        ("invalid_user", "secret_sauce", "Username and password do not match"),
        ("standard_user", "wrong_password", "Username and password do not match"),
        ("", "", "Username is required"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
    ],
)
def test_invalid_login_messages(driver, base_url, username, password, expected):
    LoginPage(driver).load(base_url).login(username, password)
    assert expected in LoginPage(driver).error_message()


@pytest.mark.regression
@pytest.mark.login
def test_locked_out_user(driver, base_url):
    LoginPage(driver).load(base_url).login("locked_out_user", "secret_sauce")
    assert "locked out" in LoginPage(driver).error_message().lower()
