from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import BasePage


class InventoryPage(BasePage):
    INVENTORY_CONTAINER = (By.ID, "inventory_container")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    ITEM_PRICES = (By.CLASS_NAME, "inventory_item_price")

    def is_loaded(self) -> bool:
        return self.find(self.INVENTORY_CONTAINER).is_displayed()

    def add_item_by_name(self, item_name: str):
        kebab_name = item_name.lower().replace(" ", "-")
        locator = (By.ID, f"add-to-cart-{kebab_name}")
        self.click(locator)

    def get_cart_count(self) -> int:
        elements = self.driver.find_elements(*self.CART_BADGE)
        return int(elements[0].text) if elements else 0

    def go_to_cart(self):
        self.click(self.CART_LINK)

    def sort_products_by(self, visible_text: str):
        select = Select(self.find(self.SORT_DROPDOWN))
        select.select_by_visible_text(visible_text)

    def get_all_prices(self) -> list[float]:
        price_elements = self.find_all(self.ITEM_PRICES)
        return [float(p.text.replace("$", "")) for p in price_elements]
