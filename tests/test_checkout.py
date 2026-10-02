import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

def checkout_page(driver, base_url, credentials):
    LoginPage(driver).open(base_url).login(credentials["username"], credentials["password"])
    inventory = InventoryPage(driver)
    inventory.add_product_by_name("Sauce Labs Backpack")
    inventory.open_cart()
    CartPage(driver).checkout()
    return CheckoutPage(driver)

@pytest.mark.checkout
def test_checkout_information_page_loads(driver, base_url, credentials):
    assert checkout_page(driver, base_url, credentials).is_loaded()

@pytest.mark.checkout
def test_checkout_requires_first_name(driver, base_url, credentials):
    page = checkout_page(driver, base_url, credentials)
    page.fill_info("", "Tester", "411001")
    page.continue_checkout()
    assert "First Name is required" in page.error_message()

@pytest.mark.checkout
def test_checkout_requires_last_name(driver, base_url, credentials):
    page = checkout_page(driver, base_url, credentials)
    page.fill_info("QA", "", "411001")
    page.continue_checkout()
    assert "Last Name is required" in page.error_message()

@pytest.mark.checkout
def test_checkout_requires_postal_code(driver, base_url, credentials):
    page = checkout_page(driver, base_url, credentials)
    page.fill_info("QA", "Tester", "")
    page.continue_checkout()
    assert "Postal Code is required" in page.error_message()

@pytest.mark.checkout
def test_checkout_cancel_returns_to_cart(driver, base_url, credentials):
    page = checkout_page(driver, base_url, credentials)
    page.cancel()
    assert CartPage(driver).is_loaded()

@pytest.mark.checkout
def test_successful_checkout(driver, base_url, credentials):
    page = checkout_page(driver, base_url, credentials)
    page.fill_info("QA", "Tester", "411001")
    page.continue_checkout()
    page.finish()
    assert page.confirmation() == "Thank you for your order!"
