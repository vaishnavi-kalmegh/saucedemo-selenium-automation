import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage


@pytest.mark.cart
def test_add_backpack_to_cart(logged_in):
    logged_in.add_backpack_to_cart()
    assert logged_in.get_cart_count() == "1"


@pytest.mark.cart
def test_add_bike_light_to_cart(logged_in):
    logged_in.add_bike_light_to_cart()
    assert logged_in.get_cart_count() == "1"


@pytest.mark.cart
def test_add_two_items_to_cart(logged_in):
    logged_in.add_backpack_to_cart()
    logged_in.add_bike_light_to_cart()
    assert logged_in.get_cart_count() == "2"


@pytest.mark.cart
def test_remove_backpack_from_inventory_updates_cart(logged_in):
    logged_in.add_backpack_to_cart()
    assert logged_in.get_cart_count() == "1"
    logged_in.remove_backpack()
    assert not logged_in.cart_badge_is_visible()


@pytest.mark.cart
def test_remove_backpack_from_cart_empties_cart(logged_in):
    logged_in.add_backpack_to_cart()
    logged_in.go_to_cart()
    cart = CartPage(logged_in.driver)
    cart.remove_backpack()
    assert cart.is_empty()


@pytest.mark.cart
def test_continue_shopping_returns_to_inventory(logged_in):
    logged_in.add_backpack_to_cart()
    logged_in.go_to_cart()
    CartPage(logged_in.driver).continue_shopping()
    assert InventoryPage(logged_in.driver).is_inventory_displayed()
