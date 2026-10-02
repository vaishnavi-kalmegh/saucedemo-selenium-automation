import os
import pytest
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser: chrome or firefox"
    )
    parser.addoption(
        "--headless", action="store_true", default=False, help="Run browser in headless mode"
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
        service = ChromeService(ChromeDriverManager().install())
        web_driver = webdriver.Chrome(service=service, options=options)

    elif browser_name == "firefox":
        options = webdriver.FirefoxOptions()
        if is_headless:
            options.add_argument("-headless")
        service = FirefoxService(GeckoDriverManager().install())
        web_driver = webdriver.Firefox(service=service, options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    web_driver.maximize_window()
    yield web_driver
    web_driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """Takes a screenshot automatically when an assertion or locator fails."""
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = os.path.join(os.getcwd(), "screenshots")
            os.makedirs(screenshots_dir, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"{item.name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            driver.save_screenshot(file_path)

            try:
                import allure
                allure.attach.file(
                    file_path,
                    name="Failure Screenshot",
                    attachment_type=allure.attachment_type.PNG
                )
            except ImportError:
                pass
