import time

from pages.login_page import LoginPage
from pages.doctor_dashboard_page import DoctorDashboardPage

def test_invalid_login(driver):
    """
    Negative Test: Verifies that incorrect credentials trigger the error message.
    """
    login_page = LoginPage(driver)
    login_page.load()

    # Execute login with intentionally wrong credentials
    login_page.login("wronguser@example.com", "wrongpassword123")

    # Assert that the error message appears and matches the expected text
    error_text = login_page.get_error_message()
    assert error_text == "Invalid login credentials", f"Expected 'Invalid login credentials', but got '{error_text}'"


def test_valid_login(driver):
    """
    Positive Test: Verifies that valid credentials successfully authenticate the user, accepts the consent popup and loads the dashboard.
    """
    login_page = LoginPage(driver)
    login_page.load()

    # execcuting login with actual credentials
    login_page.login("email@gmail.com", "123")

    # handle consent popup
    login_page.accept_consent_popup()

    time.sleep(0.5)
    dashboard_page = DoctorDashboardPage(driver)

    # Assert that the stats card appears
    assert dashboard_page.is_dashboard_loaded() == True, "Dashboard failed to load after login!"
