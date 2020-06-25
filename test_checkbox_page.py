from .pages.main_page import MainPage
from .pages.checkbox_page import CheckBox
from .credentials import link


def test_fill_form_in_autocomplete(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_datepicker()
    checkbox_page = CheckBox(browser, browser.current_url)
    checkbox_page.check_all_boxes()

