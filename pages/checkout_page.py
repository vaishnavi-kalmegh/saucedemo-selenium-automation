from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class CheckoutPage(BasePage):
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    CANCEL_BUTTON = (By.ID, "cancel")
    FINISH_BUTTON = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    CHECKOUT_OVERVIEW_TITLE = (By.CLASS_NAME, "title")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")
    SUMMARY_TOTAL = (By.CLASS_NAME, "summary_total_label")

    def fill_shipping_information(self, first_name: str, last_name: str, postal_code: str):
        self.enter_text(self.FIRST_NAME_INPUT, first_name)
        self.enter_text(self.LAST_NAME_INPUT, last_name)
        self.enter_text(self.POSTAL_CODE_INPUT, postal_code)
        self.click(self.CONTINUE_BUTTON)

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)

    def cancel_checkout(self):
        self.click(self.CANCEL_BUTTON)
        self.wait_for_url("cart.html")

    def get_completion_header_text(self) -> str:
        return self.get_text(self.COMPLETE_HEADER)

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def get_summary_total(self) -> float:
        text = self.get_text(self.SUMMARY_TOTAL)
        return float(text.split("$")[-1])

    def is_overview_displayed(self) -> bool:
        return self.get_text(self.CHECKOUT_OVERVIEW_TITLE) == "Checkout: Overview"
