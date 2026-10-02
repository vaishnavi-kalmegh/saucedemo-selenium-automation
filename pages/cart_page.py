from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def get_cart_item_names(self):
        return [item.text.strip() for item in self.driver.find_elements(*self.ITEM_NAME)]

    def get_cart_item_count(self) -> int:
        return len(self.driver.find_elements(*self.CART_ITEM))

    def is_empty(self) -> bool:
        return self.get_cart_item_count() == 0

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)

    def continue_shopping(self):
        self.click(self.CONTINUE_SHOPPING_BUTTON)
