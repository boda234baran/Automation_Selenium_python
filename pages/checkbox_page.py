from .base_page import BasePage
from .locators import CheckboxLocators

class CheckBox(BasePage):
    def check_all_boxes(self):
        self.browser.find_element_by_css_selector(CheckboxLocators.CHECK_ONE).click()
        self.browser.find_element_by_css_selector(CheckboxLocators.CHECK_TWO).click()
        self.browser.find_element_by_css_selector(CheckboxLocators.CHECK_THREE).click()