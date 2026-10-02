import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.login
def test_valid_login(driver, base_url, credentials):
    LoginPage(driver).open(base_url).login(credentials["username"], credentials["password"])
    assert InventoryPage(driver).is_loaded()

@pytest.mark.login
@pytest.mark.parametrize("username,password,expected", [
    ("invalid_user", "secret_sauce", "Username and password do not match"),
    ("standard_user", "wrong_password", "Username and password do not match"),
    ("", "", "Username is required"),
    ("", "secret_sauce", "Username is required"),
])
def test_invalid_login_messages(driver, base_url, username, password, expected):
    page = LoginPage(driver).open(base_url)
    page.login(username, password)
    assert expected in page.error_message()

@pytest.mark.login
def test_locked_out_user(driver, base_url):
    page = LoginPage(driver).open(base_url)
    page.login("locked_out_user", "secret_sauce")
    assert "locked out" in page.error_message().lower()
