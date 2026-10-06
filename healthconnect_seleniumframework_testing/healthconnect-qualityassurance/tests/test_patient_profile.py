import time

from config import Config
from pages.login_page import LoginPage
from pages.patient_dashboard_page import PatientDashboardPage
from pages.patient_profile_page import PatientProfilePage


def test_patient_update_profile(driver):
    """
    End-to-End Test: Patient navigates to their profile and updates personal details.
    """
    # login Flow
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.PATIENT_EMAIL, Config.PATIENT_PASSWORD)
    login_page.accept_consent_popup()

    time.sleep(1)

    # dashboard Navigation
    dashboard = PatientDashboardPage(driver)
    assert dashboard.is_dashboard_loaded() == True, "Patient dashboard did not load!"

    # click 'My Profile' in the navigation menu
    dashboard.go_to_profile()

    # profile Update Flow
    profile_page = PatientProfilePage(driver)
    assert profile_page.is_page_loaded() == True, "Profile page did not load!"

    profile_page.update_profile("Naani", "29")

    time.sleep(2)