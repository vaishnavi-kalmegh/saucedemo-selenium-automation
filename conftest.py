import os
from datetime import datetime

import pytest
from selenium import webdriver


BASE_URL = "https://www.saucedemo.com/"
STANDARD_USER = "standard_user"
STANDARD_PASSWORD = "secret_sauce"


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        choices=("chrome", "firefox"),
        help="Browser to run tests with: chrome or firefox",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Run the selected browser in headless mode",
    )
    parser.addoption(
        "--base-url",
        action="store",
        default=BASE_URL,
        help="Base URL for SauceDemo",
    )


@pytest.fixture(scope="function")
def driver(request):
    browser_name = request.config.getoption("--browser").lower()
    is_headless = request.config.getoption("--headless")

    if browser_name == "chrome":
        options = webdriver.ChromeOptions()
        if is_headless:
            options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-gpu")
        web_driver = webdriver.Chrome(options=options)
    else:
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        options.add_argument("--width=1920")
        options.add_argument("--height=1080")
        web_driver = webdriver.Firefox(options=options)

    web_driver.set_window_size(1920, 1080)
    yield web_driver
    web_driver.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption("--base-url").rstrip("/") + "/"


@pytest.fixture
def credentials():
    return {"username": STANDARD_USER, "password": STANDARD_PASSWORD}


@pytest.fixture
def logged_in(driver, base_url, credentials):
    from pages.login_page import LoginPage

    LoginPage(driver).load(base_url).login(
        credentials["username"], credentials["password"]
    )
    return driver


def _capture_failure(driver, test_name):
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    file_path = os.path.join(screenshots_dir, f"{test_name}_{timestamp}.png")
    driver.save_screenshot(file_path)
    return file_path


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        test_driver = item.funcargs.get("driver")
        if test_driver:
            file_path = _capture_failure(test_driver, item.name)
            try:
                import allure

                allure.attach.file(
                    file_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG,
                )
            except ImportError:
                pass
