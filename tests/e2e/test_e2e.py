import pytest
from playwright.sync_api import expect

BASE_URL = "http://127.0.0.1:8000"

@pytest.mark.e2e
def test_hello_world(page, fastapi_server):
    page.goto(BASE_URL)
    expect(page.locator("h1")).to_have_text("Hello World")

@pytest.mark.e2e
def test_calculator_add(page, fastapi_server):
    page.goto(BASE_URL)
    page.fill("#a", "10")
    page.fill("#b", "5")
    page.get_by_role("button", name="Add").click()
    expect(page.locator("#result")).to_contain_text("15")

@pytest.mark.e2e
def test_calculator_divide_by_zero(page, fastapi_server):
    page.goto(BASE_URL)
    page.fill("#a", "10")
    page.fill("#b", "0")
    page.get_by_role("button", name="Divide").click()
    expect(page.locator("#result")).to_have_text("Error: Cannot divide by zero!")