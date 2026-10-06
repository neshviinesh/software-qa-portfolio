import time
from pages.login_page import LoginPage
from pages.doctor_dashboard_page import DoctorDashboardPage
from pages.doctor_personal_profile_page import DoctorPersonalProfilePage

from config import Config

def test_doctor_update_personal_profile(driver):
    """
    End-to-End Test: Doctor navigates to their profile and updates professional details.
    """
    # Login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.DOCTOR_EMAIL, Config.DOCTOR_PASSWORD)
    login_page.accept_consent_popup()

    time.sleep(1)

    # Dashboard Navigation
    dashboard = DoctorDashboardPage(driver)
    assert dashboard.is_dashboard_loaded() == True, "Doctor dashboard did not load!"

    dashboard.go_to_profile()

    # Profile Update Flow
    profile_page = DoctorPersonalProfilePage(driver)
    assert profile_page.is_page_loaded() == True, "Doctor personal profile page did not load!"

    # Clear the old data and inject the new details
    profile_page.update_profile("Ali", "7", "English, Malay")

    time.sleep(2)