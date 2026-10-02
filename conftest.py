import os
from pathlib import Path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL", "https://www.saucedemo.com/")

@pytest.fixture(scope="session")
def credentials():
    return {
        "username": os.getenv("SAUCE_USERNAME", "standard_user"),
        "password": os.getenv("SAUCE_PASSWORD", "secret_sauce"),
    }

@pytest.fixture
def driver(request):
    options = Options()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1200")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(0)
    yield driver
    if getattr(request.node, "rep_call", None) and request.node.rep_call.failed:
        Path("reports/screenshots").mkdir(parents=True, exist_ok=True)
        safe_name = request.node.nodeid.replace("/", "_").replace("::", "_").replace("[", "_").replace("]", "_")
        driver.save_screenshot(f"reports/screenshots/{safe_name}.png")
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, f"rep_{rep.when}", rep)
