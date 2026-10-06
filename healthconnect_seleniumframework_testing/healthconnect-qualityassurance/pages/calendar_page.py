import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class CalendarPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # LOCATORS
        self.date_input = (By.CSS_SELECTOR, "input[type='date'].pd-input")
        self.confirm_btn = (By.XPATH, "//button[contains(@class, 'pd-btn-primary') and contains(text(), 'Confirm Booking')]")

    def is_page_loaded(self):
        try:
            self.wait_for_element(self.date_input, timeout=10)
            return True
        except:
            return False

    def enter_date(self, date_string):
        """
        React State Injection: Bypasses the native Chrome popup entirely.
        """
        element = self.wait_for_element(self.date_input)

        react_injection = """
            let input = arguments[0];
            let value = arguments[1];
            let nativeSetter = Object.getOwnPropertyDescriptor(window.HTMLInputElement.prototype, 'value').set;
            nativeSetter.call(input, value);
            input.dispatchEvent(new Event('input', { bubbles: true }));
            input.dispatchEvent(new Event('change', { bubbles: true }));
        """

        self.driver.execute_script(react_injection, element, date_string)
        time.sleep(2)

    def select_time_slot(self, time_text):
        slot_xpath = (By.XPATH, f"//button[contains(@class, 'pd-slot') and contains(., '{time_text}')]")
        element = self.wait.until(EC.element_to_be_clickable(slot_xpath))
        self.driver.execute_script("arguments[0].click();", element)

    def confirm_booking(self):
        self.click_element(self.confirm_btn)