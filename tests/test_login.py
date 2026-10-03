import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.mark.login
def test_valid_login_opens_inventory(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login(credentials["username"], credentials["password"])
    assert InventoryPage(driver).is_inventory_displayed()


@pytest.mark.login
def test_login_rejects_invalid_username(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login("invalid_user", credentials["password"])
    assert "Username and password do not match" in LoginPage(driver).get_error_message()


@pytest.mark.login
def test_login_rejects_invalid_password(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login(credentials["username"], "wrong_password")
    assert "Username and password do not match" in LoginPage(driver).get_error_message()


@pytest.mark.login
def test_login_requires_username(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login("", credentials["password"])
    assert "Username is required" in LoginPage(driver).get_error_message()


@pytest.mark.login
def test_login_requires_password(driver, base_url, credentials):
    LoginPage(driver).load(base_url).login(credentials["username"], "")
    assert "Password is required" in LoginPage(driver).get_error_message()


@pytest.mark.login
def test_locked_out_user_cannot_login(driver, base_url):
    LoginPage(driver).load(base_url).login("locked_out_user", "secret_sauce")
    assert "locked out" in LoginPage(driver).get_error_message().lower()
