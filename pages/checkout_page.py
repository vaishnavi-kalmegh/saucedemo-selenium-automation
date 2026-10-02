from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def fill_shipping_information(self, first_name: str, last_name: str, postal_code: str):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def get_completion_header_text(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
