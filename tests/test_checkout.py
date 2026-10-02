import pytest

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage


@pytest.fixture(autouse=True)
def setup_cart_with_item(driver, base_url, credentials):
    from pages.login_page import LoginPage

    LoginPage(driver).load(base_url).login(
        credentials["username"], credentials["password"]
    )
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()
    CartPage(driver).proceed_to_checkout()


@pytest.mark.smoke
@pytest.mark.checkout
def test_successful_checkout(driver):
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_information("Jane", "Doe", "94016")
    assert checkout.is_overview_displayed()

    checkout.finish_checkout()
    assert checkout.get_completion_header_text() == "Thank you for your order!"


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_missing_postal_code(driver):
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_information("Jane", "Doe", "")

    assert "Postal Code is required" in checkout.get_error_message()


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_missing_first_name(driver):
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_information("", "Doe", "94016")

    assert "First Name is required" in checkout.get_error_message()


@pytest.mark.regression
@pytest.mark.checkout
def test_checkout_missing_last_name(driver):
    checkout = CheckoutPage(driver)
    checkout.fill_shipping_information("Jane", "", "94016")

    assert "Last Name is required" in checkout.get_error_message()


@pytest.mark.regression
@pytest.mark.checkout
def test_cancel_checkout_returns_to_inventory(driver):
    checkout = CheckoutPage(driver)
    checkout.cancel_checkout()

    assert InventoryPage(driver).is_inventory_displayed()
