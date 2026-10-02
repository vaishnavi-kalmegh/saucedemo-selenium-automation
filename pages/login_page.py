from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[data-test='error']")

    def load(self, url: str = "https://www.saucedemo.com/"):
        self.open_url(url)
        return self

    def open(self, url: str):
        return self.load(url)

    def login(self, username: str, password: str):
        self.enter_text(self.USERNAME_INPUT, username)
        self.enter_text(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
        return self

    def error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)

    def get_error_message(self) -> str:
        return self.error_message()
