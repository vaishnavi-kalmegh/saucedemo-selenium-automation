import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@pytest.fixture(autouse=True)
def setup_logged_in_user(driver, base_url, credentials):
    from pages.login_page import LoginPage

    LoginPage(driver).load(base_url).login(
        credentials["username"], credentials["password"]
    )


@pytest.mark.smoke
@pytest.mark.cart
def test_add_item_to_cart(driver):
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()

    assert inventory.get_cart_count() == "1"

    inventory.go_to_cart()
    assert "Sauce Labs Backpack" in CartPage(driver).get_cart_item_names()


@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_from_cart(driver):
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    cart = CartPage(driver)
    cart.remove_backpack()

    assert cart.is_empty()


@pytest.mark.regression
@pytest.mark.cart
def test_add_multiple_items_to_cart(driver):
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.add_bike_light_to_cart()

    assert inventory.get_cart_count() == "2"

    inventory.go_to_cart()
    assert CartPage(driver).get_cart_item_count() == 2


@pytest.mark.regression
@pytest.mark.cart
def test_continue_shopping_returns_to_inventory(driver):
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    inventory.go_to_cart()

    CartPage(driver).continue_shopping()
    assert InventoryPage(driver).is_inventory_displayed()


@pytest.mark.regression
@pytest.mark.cart
def test_remove_item_updates_cart_badge(driver):
    inventory = InventoryPage(driver)
    inventory.add_backpack_to_cart()
    assert inventory.get_cart_count() == "1"

    inventory.remove_backpack()
    assert not inventory.cart_badge_is_visible()
