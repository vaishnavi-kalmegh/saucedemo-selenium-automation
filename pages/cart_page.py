from selenium.webdriver.common.by import By
from .base_page import BasePage

class CartPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    CART_ITEMS = (By.CSS_SELECTOR, ".cart_item")
    ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")
    REMOVE_BUTTONS = (By.CSS_SELECTOR, "button[data-test^='remove']")
    CONTINUE = (By.ID, "continue-shopping")
    CHECKOUT = (By.ID, "checkout")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Your Cart"

    def item_names(self):
        return [e.text for e in self.driver.find_elements(*self.ITEM_NAMES)]

    def item_count(self):
        return len(self.driver.find_elements(*self.CART_ITEMS))

    def remove_first(self):
        self.click(self.REMOVE_BUTTONS)

    def continue_shopping(self):
        self.click(self.CONTINUE)

    def checkout(self):
        self.click(self.CHECKOUT)
