from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ITEM = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")
    REMOVE_BACKPACK_BUTTON = (By.ID, "remove-sauce-labs-backpack")

    def _wait_for_cart_page(self):
        self.wait.until(EC.url_contains("cart.html"))
        self.wait.until(
            EC.presence_of_element_located((By.ID, "cart_contents_container"))
        )

    def get_cart_item_names(self):
        self._wait_for_cart_page()
        return [item.text.strip() for item in self.driver.find_elements(*self.ITEM_NAME)]

    def get_cart_item_count(self):
        self._wait_for_cart_page()
        return len(self.driver.find_elements(*self.CART_ITEM))

    def is_empty(self):
        return self.get_cart_item_count() == 0

    def remove_backpack(self):
        self._wait_for_cart_page()
        self.click(self.REMOVE_BACKPACK_BUTTON)
        self.wait_until_invisible(self.CART_ITEM)

    def proceed_to_checkout(self):
        self._wait_for_cart_page()
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-one.html")

    def continue_shopping(self):
        self._wait_for_cart_page()
        self.click(self.CONTINUE_SHOPPING_BUTTON)
        self.wait_for_url("inventory.html")
