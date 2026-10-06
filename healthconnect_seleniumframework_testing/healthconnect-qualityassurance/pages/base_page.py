from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from config import Config


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        # Default wait time of 10 seconds for all actions
        self.wait = WebDriverWait(self.driver, Config.EXPLICIT_WAIT)

    def click_element(self, locator):
        """Waits for an element to be clickable, then clicks it."""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def enter_text(self, locator, text):
        """Waits for an element to be visible, clears it, and types text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        """Waits for an element to be visible and returns its text."""
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_element_displayed(self, locator):
        """Checks if an element is currently displayed on the page."""
        try:
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.is_displayed()
        except:
            return False

    def select_react_dropdown(self, dropdown_locator, option_text):
        """
        Handles custom React dropdowns.
        Clicks the dropdown to open it, then clicks the specific text option.
        """
        # Click the main dropdown to open the menu
        self.click_element(dropdown_locator)

        # Find the specific option in the list by its text and click it
        option_locator = (By.XPATH, f"//div[text()='{option_text}'] | //li[text()='{option_text}'] | //span[text()='{option_text}']")
        self.click_element(option_locator)

    def select_html_dropdown(self, locator, visible_text):
        """
        Handles standard HTML <select> dropdowns.
        Finds the dropdown, and selects the option matching the visible text.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        dropdown = Select(element)
        dropdown.select_by_visible_text(visible_text)

    def wait_for_element(self, locator, timeout=Config.EXPLICIT_WAIT):
        """
        Explicitly waits up to 'timeout' seconds for an element to be visible.
        Returns the element if found, or raises a TimeoutException if it never appears.
        """
        custom_wait = WebDriverWait(self.driver, timeout)
        return custom_wait.until(EC.visibility_of_element_located(locator))

    def js_click(self, locator):
        """
        Executes a click directly via JavaScript.
        Highly effective for React/Angular apps where standard clicks get intercepted.
        """
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)