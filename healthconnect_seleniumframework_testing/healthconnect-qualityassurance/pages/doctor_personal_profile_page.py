import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class DoctorPersonalProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # LOCATORS
        # Targets the text input that is strictly required : name
        self.name_input = (By.CSS_SELECTOR, "input.pd-input[type='text'][required]")

        # years of experience
        self.yoe_input = (By.CSS_SELECTOR, "input.pd-input[type='number'][min='0']")

        # languages spoken
        self.lang_input = (By.CSS_SELECTOR, "input.pd-input[type='text']:not([required])")

        # Save button
        self.save_btn = (By.XPATH, "//button[contains(@class, 'pd-save-btn') and contains(., 'Save Changes')]")

    def is_page_loaded(self):
        try:
            self.wait_for_element(self.name_input, timeout=10)
            return True
        except:
            return False

    def clear_and_type(self, locator, text):
        """Selects all existing text, deletes it, and types the new text."""
        element = self.wait_for_element(locator)

        import sys
        if sys.platform == 'darwin':
            element.send_keys(Keys.COMMAND + "a")
        else:
            element.send_keys(Keys.CONTROL + "a")

        time.sleep(0.2)
        element.send_keys(Keys.BACKSPACE)
        time.sleep(0.2)

        element.send_keys(text)

    def update_profile(self, name, yoe, languages):
        """Updates the doctor's profile fields and saves."""
        self.clear_and_type(self.name_input, name)
        self.clear_and_type(self.yoe_input, str(yoe))
        self.clear_and_type(self.lang_input, languages)

        self.js_click(self.save_btn)