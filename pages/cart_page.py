from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def get_cart_item_names(self) -> list[str]:
        items = self.find_all(self.ITEM_NAME)
        return [item.text for item in items]

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
