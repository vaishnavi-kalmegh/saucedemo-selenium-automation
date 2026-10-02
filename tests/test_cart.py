import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage

def login(driver, base_url, credentials):
    LoginPage(driver).open(base_url).login(credentials["username"], credentials["password"])
    return InventoryPage(driver)

@pytest.mark.cart
def test_add_one_product_to_cart(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    inventory.add_product_by_name("Sauce Labs Backpack")
    assert inventory.cart_count() == 1

@pytest.mark.cart
def test_add_multiple_products_to_cart(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    for name in ["Sauce Labs Backpack", "Sauce Labs Bike Light"]:
        inventory.add_product_by_name(name)
    assert inventory.cart_count() == 2

@pytest.mark.cart
def test_remove_product_from_inventory(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    inventory.add_product_by_name("Sauce Labs Backpack")
    inventory.remove_product_by_name("Sauce Labs Backpack")
    assert not inventory.driver.find_elements(*inventory.CART_BADGE)

@pytest.mark.cart
def test_cart_contains_added_product(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    inventory.add_product_by_name("Sauce Labs Backpack")
    inventory.open_cart()
    assert CartPage(driver).item_names() == ["Sauce Labs Backpack"]

@pytest.mark.cart
def test_remove_product_from_cart(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    inventory.add_product_by_name("Sauce Labs Backpack")
    inventory.open_cart()
    cart = CartPage(driver)
    cart.remove_first()
    assert cart.item_count() == 0

@pytest.mark.cart
def test_continue_shopping_returns_to_inventory(driver, base_url, credentials):
    inventory = login(driver, base_url, credentials)
    inventory.open_cart()
    CartPage(driver).continue_shopping()
    assert InventoryPage(driver).is_loaded()
