import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from config import Config


# The data matrix: (email, password, expected_error_text, scenario_name)
@pytest.mark.parametrize(
    "email, password, expected_error, scenario",
    [
        ("fake@doctor.com", "Password123!", "Invalid credentials", "Wrong Email"),
        (Config.DOCTOR_EMAIL, "wrongpass", "Invalid credentials", "Wrong Password"),
        ("", "Password123!", "Email is required", "Empty Email"),
        (Config.DOCTOR_EMAIL, "", "Password is required", "Empty Password"),
    ]
)
def test_negative_login_flows(driver, email, password, expected_error, scenario):
    """Validates that invalid login attempts trigger the correct error messages."""
    login_page = LoginPage(driver)
    login_page.load()
    login_page.accept_consent_popup()

    login_page.login(email, password)

    error_locator = (By.CSS_SELECTOR, ".text-red-500")

    # wait for ui to display error
    error_element = WebDriverWait(driver, 5).until(EC.visibility_of_element_located(error_locator))

    # assert the expected text is actually inside the error element
    assert expected_error in error_element.text, f"Failed on scenario: {scenario}"