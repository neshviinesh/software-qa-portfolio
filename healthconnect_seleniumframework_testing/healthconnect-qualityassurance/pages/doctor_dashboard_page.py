from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DoctorDashboardPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.dashboard_subtitle = (By.CSS_SELECTOR, "p.pd-page-sub")
        self.book_appointment_btn = (By.CSS_SELECTOR, "a[href='/book']")
        self.join_teleconsult_btn = (By.CSS_SELECTOR, "a[href='/room']")

        # locator for availability btn
        self.availability_btn = (By.CSS_SELECTOR, "a[href='/doctor/availability']")
        # locator for profile page
        self.profile_nav_link = (By.CSS_SELECTOR, "a[href='/profile/doctor']")

    def is_dashboard_loaded(self):
        """Checks if the dashboard successfully loaded."""
        return self.is_element_displayed(self.dashboard_subtitle)

    def click_book_appointment(self):
        self.click_element(self.book_appointment_btn)

    def click_join_teleconsult(self):
        self.click_element(self.join_teleconsult_btn)

    def go_to_availability(self):
        """Clicks the Availability nav item in the sidebar."""
        self.click_element(self.availability_btn)

    def go_to_profile(self):
        self.js_click(self.profile_nav_link)