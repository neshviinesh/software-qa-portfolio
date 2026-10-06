import time

from config import Config
from pages.login_page import LoginPage
from pages.patient_dashboard_page import PatientDashboardPage


def test_patient_log_vitals_flow(driver):
    """
    End-to-End Test: Patient logs in and successfully records daily health vitals.
    """
    # login flow
    login_page = LoginPage(driver)
    login_page.load()
    login_page.login(Config.PATIENT_EMAIL, Config.PATIENT_PASSWORD)
    login_page.accept_consent_popup()
    # allow page transition
    time.sleep(1)

    # patient dashboard flow
    dashboard = PatientDashboardPage(driver)
    assert dashboard.is_dashboard_loaded() == True, "Patient dashboard did not load!"

    # log vitals flow
    dashboard.open_log_vitals_form()

    # pass data: weight, BP, temp, heart rate, SpO2
    dashboard.log_all_vitals("71.0", "118/79", "36.6", "72", "99")

    # wait briefly to visually confirm the submission before the test closes
    time.sleep(2)