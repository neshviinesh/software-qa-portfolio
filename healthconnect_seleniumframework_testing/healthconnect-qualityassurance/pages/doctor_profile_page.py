from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DoctorProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # locator for book btn
        self.profile_book_btn = (By.CSS_SELECTOR, "button.pd-book-btn")

    def is_page_loaded(self):
        """Verifies we successfully navigated to the profile page."""
        try:
            self.wait_for_element(self.profile_book_btn, timeout=10)
            return True
        except:
            return False

    def click_book_appointment(self):
        # use JS click
        self.js_click(self.profile_book_btn)