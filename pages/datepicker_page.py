from .base_page import BasePage
from .locators import DatepickerLocators


class DatePicker(BasePage):
   def chose_date_of_birthday(self):
       date_fill = self.browser.find_element_by_css_selector(DatepickerLocators.INPUT_DATEPICHER)
       date_fill.send_keys('09.08.1997')