from selenium.webdriver.common.by import By

from config import Config
from pages.base_page import BasePage
from selenium.common.exceptions import TimeoutException


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(f"{Config.BASE_URL}/login")

        # locators
        self.email_input = (By.CSS_SELECTOR, "input[type='email']")
        self.password_input = (By.CSS_SELECTOR, "input[type='password']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.error_message = (By.CSS_SELECTOR, "div.r-error")

        # Locator for the consent popup button
        self.agree_popup_button = (By.CSS_SELECTOR, "button.pd-btn-submit")

    def load(self):
        self.driver.get(f"{Config.BASE_URL}/login")

    def login(self, email, password):
        self.enter_text(self.email_input, email)
        self.enter_text(self.password_input, password)
        self.click_element(self.login_button)

    def accept_consent_popup(self):
        try:
            # try to click the popup
            self.click_element(self.agree_popup_button)
        except TimeoutException:
            # If it times out because the popup isn't there, just ignore it and move on
            pass
        except Exception:
            # catch any other errors so the test doesnt fail
            pass

    def get_error_message(self):
        if self.is_element_displayed(self.error_message):
            return self.get_element_text(self.error_message)
        return None