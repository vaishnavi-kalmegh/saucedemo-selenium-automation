import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(autouse=True)
def setup_cart_with_item(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

    inventory_page = InventoryPage(driver)
    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.proceed_to_checkout()

@pytest.mark.smoke
def test_successful_checkout(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_information("Jane", "Doe", "94016")
    checkout_page.finish_checkout()

    header = checkout_page.get_completion_header_text()
    assert "Thank you for your order!" in header

@pytest.mark.regression
def test_checkout_missing_postal_code(driver):
    checkout_page = CheckoutPage(driver)
    checkout_page.fill_shipping_information("Jane", "Doe", "")

    error = checkout_page.get_error_message()
    assert "Error: Postal Code is required" in error
