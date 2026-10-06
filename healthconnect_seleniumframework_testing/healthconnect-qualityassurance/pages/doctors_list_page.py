from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class DoctorsListPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        # title of page so we know the page is loaded
        self.page_header = (By.CSS_SELECTOR, "h1.pd-page-title")

    def is_page_loaded(self):
        return self.is_element_displayed(self.page_header)

    def click_book_doctor(self, doctor_name):
        doctor_book_btn_xpath = (By.XPATH, f"//h3[contains(@class, 'pd-doc-name') and text()='{doctor_name}']/ancestor::div[contains(@class, 'pd-doc-card')]//a[contains(@class, 'pd-doc-btn-book')]")

        # JS click to guarantee the click event fires
        self.js_click(doctor_book_btn_xpath)