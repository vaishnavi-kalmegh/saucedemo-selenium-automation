from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CLASS_NAME, "title")
    SHOPPING_CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SHOPPING_CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_TO_CART_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")

    def is_inventory_displayed(self) -> bool:
        return self.is_visible(self.TITLE) and self.get_text(self.TITLE) == "Products"

    def add_backpack_to_cart(self):
        self.click(self.ADD_TO_CART_BACKPACK)

    def get_cart_count(self) -> str:
        return self.get_text(self.SHOPPING_CART_BADGE)

    def go_to_cart(self):
        self.click(self.SHOPPING_CART_LINK)
