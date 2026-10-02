# SauceDemo Selenium + Python + pytest Automation

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.x-green)
![pytest](https://img.shields.io/badge/pytest-8.x-orange)
![CI](https://github.com/vaishnavi-kalmegh/saucedemo-selenium-automation/actions/workflows/tests.yml/badge.svg)

Portfolio-ready UI automation framework for SauceDemo using Selenium WebDriver, Python, pytest and Page Object Model (POM).

## What this project demonstrates

- 18 automated tests covering login, cart and checkout
- Maintainable Page Object Model
- Reusable pytest fixtures and explicit waits
- Parameterized negative testing
- Automatic screenshots on test failure
- Self-contained pytest HTML reporting
- Headless Chrome execution
- GitHub Actions CI on every push

## Test coverage

| Area | Tests |
|---|---:|
| Login | 6 |
| Cart | 6 |
| Checkout | 6 |
| **Total** | **18** |

## Framework structure

    saucedemo-selenium-automation/
    ├── .github/workflows/tests.yml
    ├── pages/
    │   ├── base_page.py
    │   ├── login_page.py
    │   ├── inventory_page.py
    │   ├── cart_page.py
    │   └── checkout_page.py
    ├── tests/
    │   ├── test_login.py
    │   ├── test_cart.py
    │   └── test_checkout.py
    ├── reports/
    ├── screenshots/
    ├── conftest.py
    ├── pytest.ini
    ├── requirements.txt
    └── README.md

## Page Object Model

BasePage centralizes common Selenium operations such as click, type and explicit waits.

LoginPage handles authentication and login errors.

InventoryPage handles products, cart badge, sorting and cart navigation.

CartPage handles cart contents, remove and checkout actions.

CheckoutPage handles customer information, validation, cancel and order completion.

Tests contain business assertions while page objects contain Selenium locators and browser actions.

## Run locally

    git clone https://github.com/vaishnavi-kalmegh/saucedemo-selenium-automation.git
    cd saucedemo-selenium-automation
    python -m venv .venv

Windows:

    .venv\\Scripts\\activate

macOS/Linux:

    source .venv/bin/activate

Install:

    pip install -r requirements.txt

Run all 18 tests:

    pytest

Run individual modules:

    pytest tests/test_login.py
    pytest tests/test_cart.py
    pytest tests/test_checkout.py

Run by marker:

    pytest -m login
    pytest -m cart
    pytest -m checkout

## HTML report

pytest-html generates:

    reports/report.html

The report is self-contained and is uploaded by GitHub Actions after every run.

## GitHub Actions

Workflow: .github/workflows/tests.yml

On every push it:

1. Checks out the repository.
2. Installs Python 3.12.
3. Installs Selenium, pytest and pytest-html.
4. Runs Chrome in headless mode through Selenium Manager.
5. Executes all 18 tests.
6. Uploads the HTML report.
7. Uploads failure screenshots when available.

The workflow also supports manual dispatch.

## Screenshots and evidence

Real browser screenshots are not fabricated or presented as execution evidence.

The framework automatically captures screenshots for failed tests under:

    reports/screenshots/

For a polished portfolio presentation, add real screenshots from an actual local or CI run:

1. SauceDemo login page
2. Inventory/cart flow
3. Checkout overview
4. pytest HTML report
5. GitHub Actions run

See screenshots/README.md for the evidence checklist.

## Configuration

Defaults:

    BASE_URL=https://www.saucedemo.com/
    SAUCE_USERNAME=standard_user
    SAUCE_PASSWORD=secret_sauce
    HEADLESS=true

These values can be overridden with environment variables.

## QA engineering practices

- Functional UI automation
- Negative testing
- End-to-end testing
- Page Object Model
- Explicit waits
- Pytest fixtures, markers and parameterization
- Failure evidence capture
- HTML reporting
- Headless browser execution
- CI/CD
- Environment-based configuration

## Execution transparency

The HTML report is a generated runtime artifact, not a fabricated committed result. GitHub Actions is configured to produce the real report on each push.

Likewise, browser screenshots should come from an actual browser execution.

## Application under test

SauceDemo: https://www.saucedemo.com/

Demo credentials:

    Username: standard_user
    Password: secret_sauce
