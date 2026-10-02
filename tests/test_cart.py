import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

@pytest.fixture(autouse=True)
def setup_logged_in_user(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login("standard_user", "secret_sauce")

@pytest.mark.smoke
def test_add_item_to_cart(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.add_backpack_to_cart()
    assert inventory_page.get_cart_count() == "1"

    inventory_page.go_to_cart()
    items = cart_page.get_cart_item_names()
    assert "Sauce Labs Backpack" in items

@pytest.mark.regression
def test_remove_item_from_cart(driver):
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)

    inventory_page.add_backpack_to_cart()
    inventory_page.go_to_cart()
    cart_page.remove_backpack()

    items = cart_page.get_cart_item_names()
    assert "Sauce Labs Backpack" not in items
