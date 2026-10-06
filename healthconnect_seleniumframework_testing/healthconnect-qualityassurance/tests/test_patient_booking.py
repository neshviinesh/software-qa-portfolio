import time

from config import Config
from pages.login_page import LoginPage
from pages.patient_dashboard_page import PatientDashboardPage
from pages.doctors_list_page import DoctorsListPage
from pages.doctor_profile_page import DoctorProfilePage
from pages.calendar_page import CalendarPage

def test_patient_booking_flow(driver):
    # login
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.PATIENT_EMAIL, Config.PATIENT_PASSWORD)
    login_page.accept_consent_popup()
    time.sleep(0.5)

    # dashboard
    dashboard = PatientDashboardPage(driver)
    assert dashboard.is_dashboard_loaded() == True, "Patient dashboard did not load!"
    dashboard.go_to_booking()

    # doctors List Page
    list_page = DoctorsListPage(driver)
    assert list_page.is_page_loaded() == True, "Doctors list page did not load!"
    list_page.click_book_doctor("Dr. Ali")

    # doctor Profile Page
    profile_page = DoctorProfilePage(driver)
    # force to wait the page is loaded
    assert profile_page.is_page_loaded() == True, "Doctor profile page did not load!"
    # click the book button to go to the calendar
    profile_page.click_book_appointment()

    # calendar Booking Flow
    calendar_page = CalendarPage(driver)
    assert calendar_page.is_page_loaded() == True, "Calendar page did not load!"

    # inject the date exactly in YYYY-MM-DD format
    calendar_page.enter_date("2026-10-15")
    # select the exact time slot
    calendar_page.select_time_slot("10:00 AM")

    # submit booking
    calendar_page.confirm_booking()