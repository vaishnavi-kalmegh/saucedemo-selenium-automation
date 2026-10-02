from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from .base_page import BasePage

class InventoryPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    SORT = (By.CSS_SELECTOR, "[data-test='product-sort-container']")
    CART_LINK = (By.CSS_SELECTOR, ".shopping_cart_link")
    CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    PRODUCT_PRICES = (By.CSS_SELECTOR, ".inventory_item_price")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Products"

    def select_sort(self, value):
        Select(self.wait.until(lambda d: d.find_element(*self.SORT))).select_by_value(value)

    def add_product_by_name(self, name):
        locator = (By.XPATH, f"//div[@class='inventory_item' and .//div[@class='inventory_item_name' and normalize-space()={repr(name)}]]//button")
        self.click(locator)

    def remove_product_by_name(self, name):
        locator = (By.XPATH, f"//div[@class='inventory_item' and .//div[@class='inventory_item_name' and normalize-space()={repr(name)}]]//button")
        self.click(locator)

    def cart_count(self):
        return int(self.get_text(self.CART_BADGE))

    def open_cart(self):
        self.click(self.CART_LINK)
