import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage


class PatientProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # locators for name and age
        self.name_input = (By.XPATH, "//input[@placeholder='Ahmad bin Abdullah']")
        self.age_input = (By.XPATH, "//input[@placeholder='e.g. 32']")

        # Locator for the save button
        self.save_btn = (By.XPATH, "//button[contains(@class, 'pd-btn-save') and contains(., 'Save Profile')]")

    def is_page_loaded(self):
        """Verifies the profile settings page rendered."""
        try:
            self.wait_for_element(self.name_input, timeout=10)
            return True
        except:
            return False

    def clear_and_type(self, locator, text):
        """
        Clears a React input field by sending Ctrl+A and Backspace,
        then types the new text.
        """
        element = self.wait_for_element(locator)


        import sys
        if sys.platform == 'darwin':
            element.send_keys(Keys.COMMAND + "a")
        else:
            element.send_keys(Keys.CONTROL + "a")

        time.sleep(0.2)
        element.send_keys(Keys.BACKSPACE)
        time.sleep(0.2)

        # Type the new text
        element.send_keys(text)

    def update_profile(self, new_name, new_age):
        """Clears existing data, enters new data, and saves."""

        # Update Name
        self.clear_and_type(self.name_input, new_name)

        # Update Age
        self.clear_and_type(self.age_input, str(new_age))

        # Click Save
        self.js_click(self.save_btn)