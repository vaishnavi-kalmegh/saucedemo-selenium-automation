from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from pages.base_page import BasePage


class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_TO_CART_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ADD_TO_CART_BOLT_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    REMOVE_BACKPACK = (By.ID, "remove-sauce-labs-backpack")

    def is_loaded(self) -> bool:
        return self.is_inventory_displayed()

    def is_inventory_displayed(self) -> bool:
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def add_bike_light_to_cart(self):
        self.click(self.ADD_TO_CART_BIKE_LIGHT)

    def add_bolt_shirt_to_cart(self):
        self.click(self.ADD_TO_CART_BOLT_SHIRT)

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK)

    def get_cart_count(self) -> str:
        return self.get_text(self.SHOPPING_CART_BADGE)

    def cart_badge_is_visible(self) -> bool:
        return self.is_visible(self.SHOPPING_CART_BADGE)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)

    def sort_by(self, option: str):
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_value(option)

    def get_product_names(self):
        return [element.text.strip() for element in self.driver.find_elements(*self.PRODUCT_NAMES)]

    def get_product_prices(self):
        return [
            float(element.text.replace("$", "").strip())
            for element in self.driver.find_elements(*self.PRODUCT_PRICES)
        ]
