# SauceDemo E-Commerce UI Test Automation Framework

An enterprise-ready UI test automation framework built to validate critical user journeys on the [SauceDemo](https://www.google.com/search?q=https://www.saucedemo.com/) web application. Designed using the **Page Object Model (POM)** pattern, this framework emphasizes high maintainability, zero arbitrary wait conditions, automated test-failure forensics, and multi-browser execution in headless CI/CD environments.

---

## Table of Contents

* Architecture and Design Principles
* Key Features
* Project Directory Structure
* Test Strategy and Coverage
* Prerequisites and Installation
* Test Execution Guide
* Reporting and Artifacts
* CI/CD Pipeline

---

## Architecture and Design Principles

```
  +-------------------------------------------------------------+
  |                        Test Layer                           |
  |    (test_login.py, test_cart.py, test_checkout.py)         |
  +------------------------------+------------------------------+
                                 | calls actions & assertions
                                 v
  +-------------------------------------------------------------+
  |                      Page Object Layer                      |
  |     (LoginPage, InventoryPage, CartPage, CheckoutPage)       |
  +------------------------------+------------------------------+
                                 | inherits
                                 v
  +-------------------------------------------------------------+
  |                          BasePage                           |
  |      (Dynamic Explicit Waits, Locator Strategy, Wrappers)   |
  +------------------------------+------------------------------+
                                 | uses
                                 v
  +-------------------------------------------------------------+
  |              Selenium WebDriver + Browser Drivers            |
  |                (Chrome, Firefox via Manager)                |
  +-------------------------------------------------------------+

```

1. **Strict Page Object Model (POM):** UI locators and web element interactions reside solely within the `pages/` directory. Test scripts (`tests/`) contain zero raw locator queries, serving strictly as high-level business flows and assertion checks.
2. **Explicit Wait Paradigm:** No `time.sleep()` is used. The framework implements encapsulated `WebDriverWait` wrappers with `expected_conditions` (such as element visibility and clickability) inside `BasePage` to eliminate test flakiness.
3. **Fixture-Driven Lifecycle:** Driver setup and teardowns are handled uniformly via Pytest fixtures with clean browser session disposal.
4. **Automated Defect Diagnostics:** Failed test cases automatically trigger screenshot capture hooks and attach snapshots to test execution reports.

---

## Key Features

* **Cross-Browser Compatibility:** Seamless switching between Google Chrome and Mozilla Firefox via CLI parameters (`--browser`).
* **Parallel Test Execution:** Integrated with `pytest-xdist` to reduce test suite runtimes across CPU cores.
* **Headless Execution for CI:** Compatible with standard headless environments (Linux agents, GitHub Actions).
* **Dual Reporting:** Generates lightweight standalone HTML reports as well as rich interactive Allure dashboards.
* **Categorized Test Suites:** Test cases tagged with `@pytest.mark.smoke` and `@pytest.mark.regression` for targeted regression and release verification.

---

## Project Directory Structure

```text
saucedemo-selenium-automation/
├── .github/
│   └── workflows/
│       └── tests.yml             # GitHub Actions CI workflow definition
├── pages/
│   ├── __init__.py
│   ├── base_page.py              # Parent page containing explicit wait abstractions
│   ├── login_page.py             # Login selectors and authentication interactions
│   ├── inventory_page.py         # Product catalog actions and inventory validations
│   ├── cart_page.py              # Cart management and quantity verification
│   └── checkout_page.py          # End-to-end checkout information and confirmation
├── tests/
│   ├── __init__.py
│   ├── test_login.py             # Authentication scenarios (positive & negative)
│   ├── test_cart.py              # Add/remove item verifications
│   └── test_checkout.py          # E2E purchase flow and tax/total assertions
├── reports/                      # Generated HTML and Allure test reports
├── screenshots/                  # Failure capture artifacts
├── conftest.py                   # Pytest hooks, CLI parameters, and browser fixtures
├── pytest.ini                   # Pytest runtime configuration and markers
├── requirements.txt              # Production and testing dependencies
└── README.md                     # Framework documentation

```

---

## Test Strategy and Coverage

| Test Module | Suite | Test Description | Assertion / Expected Outcome |
| --- | --- | --- | --- |
| `test_login` | `smoke` | Valid credential authentication | Verifies redirection to inventory and page title visibility |
| `test_login` | `regression` | Locked-out user authentication | Verifies dynamic error notification message display |
| `test_login` | `regression` | Empty username and password submission | Verifies required-field validation messages |
| `test_cart` | `smoke` | Add single item to shopping cart | Badge counter increments to 1; item appears in cart view |
| `test_cart` | `regression` | Remove item from cart and inventory | Cart badge updates dynamically and removes item container |
| `test_checkout` | `smoke` | Complete End-to-End order workflow | Order completes with "Thank you for your order!" banner |
| `test_checkout` | `regression` | Checkout with missing postal code | Prevents checkout progression and displays form validation error |

---

## Prerequisites and Installation

### 1. Prerequisites

* Python 3.10+
* Google Chrome or Mozilla Firefox installed
* Git

### 2. Setup Virtual Environment

Clone the repository:

```bash
git clone https://github.com/vaishnavi-kalmegh/saucedemo-selenium-automation.git
cd saucedemo-selenium-automation

```

Create virtual environment:

```bash
python -m venv venv

```

Activate environment:

* On macOS/Linux: `source venv/bin/activate`
* On Windows: `venv\Scripts\activate`

Install dependencies:

```bash
pip install --upgrade pip
pip install -r requirements.txt

```

---

## Test Execution Guide

### Standard Execution

Run all tests on Chrome (headed mode):

```bash
pytest

```

Run tests in headless mode:

```bash
pytest --headless

```

Run on Mozilla Firefox:

```bash
pytest --browser=firefox --headless

```

### Targeted Execution via Markers

Run only critical-path smoke tests:

```bash
pytest -m smoke

```

Run full regression suite:

```bash
pytest -m regression

```

### Parallel Execution

Run tests distributed across 3 CPU cores:

```bash
pytest -n 3 --headless

```

---

## Reporting and Artifacts

### 1. Pytest HTML Reports

Generate a single-file, self-contained HTML report:

```bash
pytest --html=reports/report.html --self-contained-html

```

### 2. Allure Interactive Reports

Generate visual test metrics, execution timelines, and attached screenshots:

```bash
pytest --alluredir=reports/allure-results
allure serve reports/allure-results

```

---

## CI/CD Pipeline

Continuous Integration is orchestrated through **GitHub Actions**. On every push and pull request to `main`:

1. Spins up an `ubuntu-latest` headless container.
2. Configures Python and installs pinned dependencies via pip cache.
3. Executes the test suite concurrently in headless Chrome.
4. Captures execution logs, test outputs, and on-failure screenshots.
5. Uploads test reports as persistent workflow artifacts.
