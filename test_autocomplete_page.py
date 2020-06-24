from .pages.main_page import MainPage
from .pages.autocomplite_page import AutocomplitePage
from .credentials import link


def test_fill_form_in_autocomplete(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_autocomplite()
    autocomplete_page = AutocomplitePage(browser, browser.current_url)
    autocomplete_page.fill_form()

