from .base_page import BasePage
from .locators import AutocompliteLocators

class AutocomplitePage(BasePage):

    def fill_form(self):
        get_email = self.browser.find_element_by_css_selector(AutocompliteLocators.EMAIL_FILL)
        get_email.send_keys(AutocompliteLocators.EMAIL_VALUE)

        get_streat_adress = self.browser.find_element_by_css_selector(AutocompliteLocators.STREAT_ADRESS_FILL)
        get_streat_adress.send_keys(AutocompliteLocators.STREAT_ADRESS_VALUE)

        get_streat_adress_2 = self.browser.find_element_by_css_selector(AutocompliteLocators.STREAT_ADRESS2_FILL)
        get_streat_adress_2.send_keys(AutocompliteLocators.STREAT_ADRESS2_VALUE)

        get_city = self.browser.find_element_by_css_selector(AutocompliteLocators.CITY_FILL)
        get_city.send_keys(AutocompliteLocators.CITY_VALUE)

        get_state = self.browser.find_element_by_css_selector(AutocompliteLocators.STATE_FILL)
        get_state.send_keys(AutocompliteLocators.STATE_VALUE)

        get_zip_code = self.browser.find_element_by_css_selector(AutocompliteLocators.ZIP_CODE_FILL)
        get_zip_code.send_keys(AutocompliteLocators.ZIP_CODE_VALUE)

        get_country = self.browser.find_element_by_css_selector(AutocompliteLocators.COUNTRY_FILL)
        get_country.send_keys(AutocompliteLocators.COUNRTY_VALUE)