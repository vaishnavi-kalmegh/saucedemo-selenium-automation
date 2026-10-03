import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@pytest.mark.checkout
def test_successful_checkout_completes_order(checkout_page):
    checkout_page.fill_shipping_information("Jane", "Doe", "94016")
    assert checkout_page.is_overview_displayed()
    checkout_page.finish_checkout()
    assert checkout_page.get_completion_header_text() == "Thank you for your order!"


@pytest.mark.checkout
def test_checkout_requires_first_name(checkout_page):
    checkout_page.fill_shipping_information("", "Doe", "94016")
    assert "First Name is required" in checkout_page.get_error_message()


@pytest.mark.checkout
def test_checkout_requires_last_name(checkout_page):
    checkout_page.fill_shipping_information("Jane", "", "94016")
    assert "Last Name is required" in checkout_page.get_error_message()


@pytest.mark.checkout
def test_checkout_requires_postal_code(checkout_page):
    checkout_page.fill_shipping_information("Jane", "Doe", "")
    assert "Postal Code is required" in checkout_page.get_error_message()


@pytest.mark.checkout
def test_cancel_checkout_returns_to_cart(checkout_page):
    checkout_page.cancel_checkout()
    assert CartPage(checkout_page.driver).get_cart_item_count() == 1


@pytest.mark.checkout
def test_checkout_overview_displays_total(checkout_page):
    checkout_page.fill_shipping_information("Jane", "Doe", "94016")
    assert checkout_page.is_overview_displayed()
    assert checkout_page.get_summary_total() > 0
