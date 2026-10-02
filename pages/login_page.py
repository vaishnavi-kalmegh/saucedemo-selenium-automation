import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@pytest.mark.smoke
def test_successful_login(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)

    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    assert inventory_page.is_inventory_displayed(), "Inventory page should be visible upon login."

@pytest.mark.regression
def test_locked_out_user_error(driver):
    login_page = LoginPage(driver)

    login_page.load()
    login_page.login("locked_out_user", "secret_sauce")

    expected_error = "Epic sadface: Sorry, this user has been locked out."
    assert expected_error in login_page.get_error_message()
