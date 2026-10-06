from selenium.webdriver.common.by import By
from pages.base_page import BasePage
import time


class PatientDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.page_title = (By.CSS_SELECTOR, "h1.pd-page-title")
        self.book_appointment_btn = (By.CSS_SELECTOR, "a[href='/doctors']")
        # locators for the log vitals card
        self.open_vitals_btn = (By.XPATH, "//button[contains(@class, 'pd-health-btn') and contains(., 'Log Vitals')]")
        self.weight_input = (By.XPATH, "//input[@placeholder='e.g. 72.5']")
        self.bp_input = (By.XPATH, "//input[@placeholder='e.g. 120/80']")
        self.temp_input = (By.XPATH, "//input[@placeholder='e.g. 36.5']")
        self.hr_input = (By.XPATH, "//input[@placeholder='e.g. 75']")
        self.oxygen_input = (By.XPATH, "//input[@placeholder='e.g. 98']")
        self.save_vitals_btn = (By.CSS_SELECTOR, "button.pd-btn-submit")

        self.profile_nav_link = (By.CSS_SELECTOR, "a[href='/profile/patient']")

    def is_dashboard_loaded(self):
        try:
            self.wait_for_element(self.page_title, timeout=10)
            return True
        except:
            return False

    def go_to_booking(self):
        self.click_element(self.book_appointment_btn)

    def open_log_vitals_form(self):
        """Clicks the initial button to reveal the vitals input form."""
        self.js_click(self.open_vitals_btn)

        # Wait for the first input field to appear
        self.wait_for_element(self.weight_input, timeout=5)

    def log_all_vitals(self, weight, bp, temp, hr, spo2):
        """Fills out the entire vitals form and submits it."""
        # Clear first then enter the new text
        self.enter_text(self.weight_input, str(weight))
        self.enter_text(self.bp_input, str(bp))
        self.enter_text(self.temp_input, str(temp))
        self.enter_text(self.hr_input, str(hr))
        self.enter_text(self.oxygen_input, str(spo2))

        self.js_click(self.save_vitals_btn)

    def go_to_profile(self):
        """Navigates from the dashboard to the patient profile settings."""
        self.js_click(self.profile_nav_link)