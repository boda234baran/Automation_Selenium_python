from .base_page import BasePage
from .locators import ButtonsLocators


class Buttons(BasePage):
    def click_buttons(self):
        #test
        self.browser.find_element_by_css_selector(ButtonsLocators.PRIMARY_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.SUCCESS_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.INFO_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.WARNING_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.DABGER_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.LINK_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.LEFT_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.MIDDLE_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.RIGHT_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.FIRST_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.SECOND_BTN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.DROPDOWN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.DROPDOWNLINK1).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.DROPDOWN).click()
        self.browser.find_element_by_css_selector(ButtonsLocators.DROPDOWNLINK2).click()

