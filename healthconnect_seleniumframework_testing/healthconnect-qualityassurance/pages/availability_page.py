import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class AvailabilityPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.page_subtitle = (By.CSS_SELECTOR, "p.pd-page-sub")

        monday_row = "//*[contains(text(), 'Monday')]/ancestor::*[contains(@class, 'flex') or contains(@class, 'row') or contains(@class, 'grid') or contains(@class, 'container')][1]"

        self.monday_toggle = (By.XPATH, f"{monday_row}//span[@class='pd-toggle-slider']")

        self.monday_start_time = (By.XPATH, f"({monday_row}//input[@type='time'])[1]")
        self.monday_end_time = (By.XPATH, f"({monday_row}//input[@type='time'])[2]")
        self.monday_duration = (By.XPATH, f"{monday_row}//select[contains(@class, 'pd-ctrl-select')]")

        self.save_button = (By.CSS_SELECTOR, "button.pd-save-btn")

    def is_page_loaded(self):
        return self.is_element_displayed(self.page_subtitle)

    def enable_monday(self):
        """Checks toggle state safely after letting React render."""
        # 1. Give React exactly 1 second to draw the time inputs on the screen
        time.sleep(1)

        # 2. Now check if they exist
        elements = self.driver.find_elements(*self.monday_start_time)

        if len(elements) > 0 and elements[0].is_displayed():
            print("Monday is already ON. Leaving it alone.")
            return

        print("Monday is OFF. Clicking toggle.")
        self.click_element(self.monday_toggle)

    def update_monday_times(self, start_time, end_time, duration_text):
        self.enter_text(self.monday_start_time, start_time)
        self.enter_text(self.monday_end_time, end_time)
        self.select_html_dropdown(self.monday_duration, duration_text)

    def save_schedule(self):
        self.click_element(self.save_button)