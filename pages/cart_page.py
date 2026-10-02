from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def get_cart_item_names(self):
        items = self.driver.find_elements(*self.ITEM_NAME)
        return [item.text.strip() for item in items]

    def remove_backpack(self):
        self.click(self.REMOVE_BACKPACK_BUTTON)

    def proceed_to_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
