from .pages.main_page import MainPage
from .pages.datepicker_page import DatePicker
from .credentials import link


def test_fill_form_in_autocomplete(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_datepicker()
    datepicker_page = DatePicker(browser, browser.current_url)
    datepicker_page.chose_date_of_birthday()
