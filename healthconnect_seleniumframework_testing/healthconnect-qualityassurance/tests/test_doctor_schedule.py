import time

from config import Config
from pages.login_page import LoginPage
from pages.doctor_dashboard_page import DoctorDashboardPage
from pages.availability_page import AvailabilityPage


def test_doctor_update_schedule(driver):
    """
    End-to-End Test: Doctor logs in, navigates to availability, and updates Monday's schedule.
    """
    # Login Flow
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.DOCTOR_EMAIL, Config.DOCTOR_PASSWORD)
    login_page.accept_consent_popup()

    time.sleep(0.5)  # Wait for blur to disappear

    # Dashboard Flow
    dashboard_page = DoctorDashboardPage(driver)
    assert dashboard_page.is_dashboard_loaded() == True, "Dashboard did not load!"

    # Navigate to the availability page
    dashboard_page.go_to_availability()

    # availability Update Flow
    availability = AvailabilityPage(driver)
    assert availability.is_page_loaded() == True, "Availability page did not load!"

    # enabling monday toggle
    availability.enable_monday()

    # Set the times and duration as exactly the format
    availability.update_monday_times("0900A", "0500P", "30 min")

    # save the changes
    availability.save_schedule()