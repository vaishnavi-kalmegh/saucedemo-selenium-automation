from selenium.webdriver.common.by import By
from .base_page import BasePage

class CheckoutPage(BasePage):
    TITLE = (By.CSS_SELECTOR, ".title")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE = (By.ID, "continue")
    CANCEL = (By.ID, "cancel")
    FINISH = (By.ID, "finish")
    ERROR = (By.CSS_SELECTOR, "[data-test='error']")
    COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    SUMMARY_TOTAL = (By.CSS_SELECTOR, ".summary_total_label")

    def is_loaded(self):
        return self.get_text(self.TITLE) == "Checkout: Your Information"

    def fill_info(self, first_name="", last_name="", postal_code=""):
        self.type(self.FIRST_NAME, first_name)
        self.type(self.LAST_NAME, last_name)
        self.type(self.POSTAL_CODE, postal_code)

    def continue_checkout(self):
        self.click(self.CONTINUE)

    def error_message(self):
        return self.get_text(self.ERROR)

    def cancel(self):
        self.click(self.CANCEL)

    def finish(self):
        self.click(self.FINISH)

    def confirmation(self):
        return self.get_text(self.COMPLETE_HEADER)
